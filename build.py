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


def _escape_latex(text):
    """
    Escapes a string for LaTeX, preserving math mode ($...$) and inline code (`...`).

    It parses the string in layers:
    1. It splits the text by math delimiters ($...$), leaving them untouched.
    2. For non-math segments, it then splits by inline code delimiters (`...`).
    3. The content of inline code is escaped and wrapped in \\texttt{}.
    4. Any remaining plain text is fully escaped.

    Args:
        text (str): The input string, possibly containing mixed content.

    Returns:
        str: The processed string, safe for LaTeX inclusion.
    """
    if text is None:
        return ""

    # Layer 1: Split by math blocks ($...$)
    parts = re.split(r"(\$.*?\$)", text)
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

            with open(generated_tex_path, "w", encoding="utf-8") as tex_file:
                section_title = base_filename.replace("_", " ").title()
                tex_file.write(f"\\subsection*{{{section_title}}}\n\n")

                if docstring:
                    escaped_docstring = _escape_latex(docstring)
                    tex_file.write("\\begin{docstring}\n")
                    tex_file.write(escaped_docstring)
                    tex_file.write("\n\\end{docstring}\n\n")

                tex_file.write("\\begin{minted}{python}\n")
                tex_file.write(source_code)
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
        try:
            result = subprocess.run(
                pdflatex_command,
                cwd=content_dir,
                capture_output=True,
                text=True,
                check=True,
                encoding="utf-8",
            )
            if "error" in result.stdout.lower():
                print(f"LaTeX compilation might have issues. Check {main_tex_file}.log")

        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print("\n--- LaTeX Compilation Failed ---", file=sys.stderr)
            log_file = os.path.join(content_dir, "pycpbook.log")
            print(
                f"Error during PDF compilation. See '{log_file}' for details.",
                file=sys.stderr,
            )
            if os.path.exists(log_file):
                with open(log_file, "r", encoding="utf-8") as f:
                    log_lines = f.readlines()
                    print("\n--- Last 20 lines of log file ---\n", file=sys.stderr)
                    sys.stderr.writelines(log_lines[-20:])
            sys.exit(1)

    final_pdf_path_src = os.path.join(content_dir, "pycpbook.pdf")
    final_pdf_path_dest = os.path.join(root_dir, "pycpbook.pdf")
    if os.path.exists(final_pdf_path_src):
        shutil.move(final_pdf_path_src, final_pdf_path_dest)
        print(f"\nPDF generated successfully: {final_pdf_path_dest}")
    else:
        print("Error: Final PDF was not found after compilation.", file=sys.stderr)
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
