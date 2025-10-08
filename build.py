"""
@description
This script serves as the primary build and utility tool for the Python Competitive
Programming Notebook (PyCPBook). It automates the key development tasks:
- Generating the final PDF document from Python source and LaTeX files.
- Running all stress tests to verify the correctness of the code library.
- Cleaning up build artifacts and temporary files.

The script uses a command-line interface to expose its functionality.

@usage
To use the script, run it from the root of the project directory with one of the
following commands:

- Build the PDF:
  python build.py pdf

- Run all stress tests:
  python build.py test

- Clean build artifacts:
  python build.py clean

@dependencies
- Python 3.8+
- A TeX distribution (e.g., TeX Live, MiKTeX) with 'pdflatex' in the system PATH.
"""

import argparse
import ast
import glob
import os
import re
import shutil
import subprocess
import sys


def _escape_latex_text_only(text):
    """
    Escapes characters with special meaning in LaTeX for plain text.
    This function should NOT be used on strings containing LaTeX commands.
    """
    if text is None:
        return ""
    return (
        text.replace("\\", r"\textbackslash ")
        .replace("{", r"\{")
        .replace("}", r"\}")
        .replace("#", r"\#")
        .replace("$", r"\$")
        .replace("%", r"\%")
        .replace("&", r"\&")
        .replace("_", r"\_")
        .replace("^", r"\textasciicircum{}")
        .replace("~", r"\textasciitilde{}")
    )


def _process_latex_part(text_part):
    """
    Escapes a single part of text (a paragraph or list item) for LaTeX,
    preserving math mode ($...$) and inline code (`...`).
    """
    if text_part is None:
        return ""

    # Layer 1: Split by math blocks ($...$)
    parts = re.split(r"(\$.*?\$)", text_part)
    final_parts = []

    for i, part in enumerate(parts):
        # Even-indexed parts are non-math text; odd-indexed are math blocks.
        if i % 2 == 1:
            final_parts.append(part)  # Keep math blocks as is
            continue

        # Layer 2: For non-math text, split by inline code blocks (`...`)
        sub_parts = re.split(r"(`.*?`)", part)
        for j, sub_part in enumerate(sub_parts):
            # Even-indexed are plain text; odd-indexed are code blocks.
            if j % 2 == 1:
                # For code blocks, strip backticks, escape content, and wrap in \texttt{}
                code_content = sub_part[1:-1]
                escaped_code = _escape_latex_text_only(code_content)
                final_parts.append(f"\\texttt{{{escaped_code}}}")
            else:
                # For plain text, escape it normally
                final_parts.append(_escape_latex_text_only(sub_part))

    return "".join(final_parts)


def _escape_latex(text):
    """
    Escapes a full docstring for LaTeX, handling paragraphs, lists, math, and code.
    Now processes mixed content blocks line-by-line to properly format lists.
    """
    if text is None:
        return ""

    # Regex to detect list items
    bullet_pattern = re.compile(r"^\s*[-*]\s+(.*)")
    enum_pattern = re.compile(r"^\s*\d+\.\s+(.*)")

    # Split the docstring into logical blocks (paragraphs or lists)
    blocks = re.split(r"\n\s*\n", text.strip())
    output_blocks = []

    for block in blocks:
        lines = [line for line in block.split("\n") if line.strip()]
        if not lines:
            continue

        # Process the block line-by-line to handle mixed content
        block_output = []
        current_list_type = None
        current_list_items = []
        current_paragraph_lines = []

        def flush_paragraph():
            """Flush accumulated paragraph lines."""
            nonlocal current_paragraph_lines
            if current_paragraph_lines:
                paragraph = " ".join(current_paragraph_lines)
                block_output.append(_process_latex_part(paragraph))
                current_paragraph_lines = []

        def flush_list():
            """Flush accumulated list items."""
            nonlocal current_list_type, current_list_items
            if current_list_items:
                if current_list_type == "bullet":
                    block_output.append("\\begin{itemize}")
                    block_output.extend(current_list_items)
                    block_output.append("\\end{itemize}")
                elif current_list_type == "enum":
                    block_output.append("\\begin{enumerate}")
                    block_output.extend(current_list_items)
                    block_output.append("\\end{enumerate}")
                current_list_items = []
                current_list_type = None

        for line in lines:
            line_stripped = line.strip()
            bullet_match = bullet_pattern.match(line_stripped)
            enum_match = enum_pattern.match(line_stripped)
            
            # Check if this is a continuation line (indented but not a new list item)
            is_continuation = (current_list_type is not None and 
                             line.startswith(('  ', '\t')) and 
                             not bullet_match and 
                             not enum_match)
            
            if bullet_match:
                # We have a bullet list item
                if current_list_type != "bullet":
                    flush_paragraph()  # Flush any pending paragraph
                    flush_list()  # Flush any existing list
                    current_list_type = "bullet"
                current_list_items.append(f"  \\item {_process_latex_part(bullet_match.group(1))}")
                
            elif enum_match:
                # We have a numbered list item
                if current_list_type != "enum":
                    flush_paragraph()  # Flush any pending paragraph
                    flush_list()  # Flush any existing list
                    current_list_type = "enum"
                current_list_items.append(f"  \\item {_process_latex_part(enum_match.group(1))}")
                
            elif is_continuation:
                # This is a continuation of the current list item
                if current_list_items:
                    # Append to the last list item
                    current_list_items[-1] += " " + _process_latex_part(line_stripped)
                
            else:
                # We have regular text
                if current_list_type is not None:
                    flush_list()  # Flush any existing list
                current_paragraph_lines.append(line_stripped)

        # Flush any remaining content
        flush_list()
        flush_paragraph()

        # Join all output from this block
        if block_output:
            output_blocks.append("\n".join(block_output))

    return "\n\\par\n".join(output_blocks)


def run_clean():
    """
    Finds and removes all temporary files created during the PDF build process,
    as well as the final PDF itself. This helps maintain a clean project directory.
    """
    print("Cleaning build artifacts...")

    patterns = [
        "*.aux",
        "*.log",
        "*.out",
        "*.toc",
        "pycpbook.pdf",
        "*.fls",
        "*.fdb_latexmk",
        "_generated_*.tex",
    ]

    root_dir = os.path.dirname(os.path.abspath(__file__))
    files_removed_count = 0

    for pattern in patterns:
        for file_path in glob.glob(os.path.join(root_dir, pattern)):
            try:
                os.remove(file_path)
                print(f"Removed: {os.path.basename(file_path)}")
                files_removed_count += 1
            except OSError as e:
                print(f"Error removing file {file_path}: {e}", file=sys.stderr)

    content_dir = os.path.join(root_dir, "content")
    for pattern in patterns:
        for file_path in glob.glob(os.path.join(content_dir, pattern)):
            try:
                os.remove(file_path)
                print(f"Removed: {os.path.basename(file_path)}")
                files_removed_count += 1
            except OSError as e:
                print(f"Error removing file {file_path}: {e}", file=sys.stderr)

    minted_path_pattern = os.path.join(root_dir, "**", "_minted*")
    minted_dirs = glob.glob(minted_path_pattern, recursive=True)
    for minted_dir in minted_dirs:
        if os.path.isdir(minted_dir):
            try:
                shutil.rmtree(minted_dir)
                print(f"Removed directory: {os.path.basename(minted_dir)}")
            except OSError as e:
                print(f"Error removing directory {minted_dir}: {e}", file=sys.stderr)

    if files_removed_count == 0 and not minted_dirs:
        print("No build artifacts found to clean.")
    else:
        print("\nClean completed successfully.")


def run_pdf():
    """
    Generates the PyCPBook PDF.

    This function scans the 'content/' directory, parses each Python file to
    extract its docstring (explanation) and code, generates intermediate LaTeX
    files, and then compiles the main 'pycpbook.tex' file into a PDF.
    """
    print("Starting PDF generation...")

    if not shutil.which("pdflatex"):
        print(
            "Error: 'pdflatex' command not found.",
            "Please install a TeX distribution (like TeX Live, MiKTeX, or MacTeX)",
            "and ensure it is in your system's PATH.",
            sep="\n",
            file=sys.stderr,
        )
        sys.exit(1)

    root_dir = os.path.dirname(os.path.abspath(__file__))
    content_dir = os.path.join(root_dir, "content")

    chapters = sorted(
        [
            d
            for d in os.listdir(content_dir)
            if os.path.isdir(os.path.join(content_dir, d))
        ]
    )

    for chapter in chapters:
        chapter_path = os.path.join(content_dir, chapter)
        py_files = sorted(glob.glob(os.path.join(chapter_path, "*.py")))
        generated_tex_files = []

        if not py_files:
            continue

        print(f"Processing chapter: {chapter}")

        for py_file_path in py_files:
            filename = os.path.basename(py_file_path)
            base_filename = os.path.splitext(filename)[0]
            generated_tex_path = os.path.join(
                chapter_path, f"_generated_{base_filename}.tex"
            )
            generated_tex_files.append(os.path.basename(generated_tex_path))

            print(f"  - Parsing {filename}...")
            with open(py_file_path, "r", encoding="utf-8") as f:
                source_code = f.read()

            try:
                tree = ast.parse(source_code)
                docstring = ast.get_docstring(tree)
            except SyntaxError as e:
                print(
                    f"Warning: Could not parse {filename}. Skipping. Error: {e}",
                    file=sys.stderr,
                )
                continue

            if not docstring:
                print(f"Warning: No docstring found in {filename}.", file=sys.stderr)

            code_to_render = source_code
            # If a docstring exists, it's the first node. Remove it from the code to render.
            if docstring and tree.body and isinstance(tree.body[0], ast.Expr):
                docstring_node = tree.body[0]

                # Verify that the node is indeed a string constant node.
                is_string_node = False
                if isinstance(docstring_node.value, ast.Constant) and isinstance(
                    docstring_node.value.value, str
                ):
                    is_string_node = True  # Python 3.8+
                elif "Str" in ast.__dict__ and isinstance(
                    docstring_node.value, ast.Str
                ):
                    is_string_node = True  # Python < 3.8 compatibility

                if is_string_node:
                    lines = source_code.splitlines(True)
                    # Get the line numbers of the docstring node.
                    start_line = docstring_node.lineno - 1
                    end_line = docstring_node.end_lineno
                    # Reconstruct the code without the docstring lines.
                    code_lines = lines[:start_line] + lines[end_line:]
                    code_to_render = "".join(code_lines).lstrip()

            with open(generated_tex_path, "w", encoding="utf-8") as tex_file:
                section_title = base_filename.replace("_", " ").title()
                tex_file.write(f"\\subsection*{{{section_title}}}\n\n")

                if docstring:
                    escaped_docstring = _escape_latex(docstring)
                    tex_file.write("\\begin{docstring}\n")
                    tex_file.write(escaped_docstring)
                    tex_file.write("\n\\end{docstring}\n\n")

                tex_file.write("\\begin{minted}{python}\n")
                tex_file.write(code_to_render)
                tex_file.write("\n\\end{minted}\n")

        chapter_tex_path = os.path.join(chapter_path, "chapter.tex")
        with open(chapter_tex_path, "w", encoding="utf-8") as f:
            f.write("% This file is automatically generated by build.py.\n")
            f.write("% Do not edit manually.\n\n")
            for generated_file in generated_tex_files:
                f.write(f"\\input{{{os.path.join(chapter, generated_file)}}}\n")

    print("\nCompiling LaTeX document...")
    main_tex_file = "pycpbook.tex"
    pdflatex_command = [
        "pdflatex",
        "--shell-escape",
        "-interaction=nonstopmode",
        main_tex_file,
    ]

    for i in range(2):
        print(f"--- Pass {i + 1} ---")
        result = subprocess.run(
            pdflatex_command,
            cwd=content_dir,
            capture_output=True,
            text=True,
            check=False,
            encoding="utf-8",
        )
        if result.returncode != 0:
            print("Warning: pdflatex returned a non-zero exit code. Checking output/logs...")
        elif "error" in (result.stdout or "").lower():
            print(f"LaTeX reported errors in output. Check {main_tex_file}.log")

    final_pdf_path_src = os.path.join(content_dir, "pycpbook.pdf")
    final_pdf_path_dest = os.path.join(root_dir, "pycpbook.pdf")
    if os.path.exists(final_pdf_path_src):
        try:
            shutil.copyfile(final_pdf_path_src, final_pdf_path_dest)
            print(f"\nPDF generated successfully: {final_pdf_path_dest}")
        except OSError as e:
            print(f"Warning: Could not copy PDF to project root: {e}", file=sys.stderr)
        print(f"PDF also available at: {final_pdf_path_src}")
    else:
        print("\n--- LaTeX Compilation Failed ---", file=sys.stderr)
        log_file = os.path.join(content_dir, "pycpbook.log")
        print(
            f"Error: Final PDF was not found after compilation. See '{log_file}' for details.",
            file=sys.stderr,
        )
        if os.path.exists(log_file):
            with open(log_file, "r", encoding="utf-8") as f:
                log_lines = f.readlines()
                print("\n--- Last 20 lines of log file ---\n", file=sys.stderr)
                sys.stderr.writelines(log_lines[-20:])
        sys.exit(1)


def run_test():
    """
    Discovers and runs all stress tests located in the 'stress_tests/' directory.
    """
    print("Running all stress tests...")
    root_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(root_dir, "stress_tests")
    utilities_dir = os.path.join(tests_dir, "utilities")

    test_files = []
    for file_path in glob.glob(os.path.join(tests_dir, "**", "*.py"), recursive=True):
        if not file_path.startswith(utilities_dir):
            test_files.append(file_path)

    if not test_files:
        print("No test files found to run.")
        return

    failed_tests = []
    for test_file in test_files:
        relative_path = os.path.relpath(test_file, root_dir)
        print(f"--- Running test: {relative_path} ---")
        try:
            result = subprocess.run(
                [sys.executable, test_file],
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            if result.stdout.strip():
                print(result.stdout)
            print(f"--- PASS: {relative_path} ---\n")
        except subprocess.CalledProcessError as e:
            print(f"--- FAIL: {relative_path} ---", file=sys.stderr)
            print("\nSTDOUT:", file=sys.stderr)
            print(e.stdout, file=sys.stderr)
            print("\nSTDERR:", file=sys.stderr)
            print(e.stderr, file=sys.stderr)
            failed_tests.append(relative_path)
            print("-" * 30, "\n", file=sys.stderr)

    if failed_tests:
        print(f"\nSummary: {len(failed_tests)} test(s) failed:", file=sys.stderr)
        for test in failed_tests:
            print(f"  - {test}", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"\nSummary: All {len(test_files)} tests passed successfully!")


def main():
    """
    Main entry point for the script.
    """
    parser = argparse.ArgumentParser(
        description="Build and utility script for the Python Competitive Programming Notebook (PyCPBook)."
    )
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    pdf_parser = subparsers.add_parser(
        "pdf", help="Parse content and generate the PDF notebook."
    )
    pdf_parser.set_defaults(func=run_pdf)

    test_parser = subparsers.add_parser(
        "test", help="Discover and run all stress tests."
    )
    test_parser.set_defaults(func=run_test)

    clean_parser = subparsers.add_parser(
        "clean", help="Clean up all build artifacts and temporary files."
    )
    clean_parser.set_defaults(func=run_clean)

    args = parser.parse_args()
    args.func()


if __name__ == "__main__":
    main()
