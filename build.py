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
import shutil
import subprocess
import sys


def _escape_latex(text):
    """
    Escapes characters with special meaning in LaTeX.

    This function ensures that plain text (like docstrings) can be safely
    included in a .tex file without causing compilation errors.

    Args:
        text (str): The input string to be escaped.

    Returns:
        str: The string with LaTeX special characters escaped.
    """
    if text is None:
        return ""
    return (
        text.replace("\\", r"\textbackslash{}")
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


def run_clean():
    """
    Finds and removes all temporary files created during the PDF build process,
    as well as the final PDF itself. This helps maintain a clean project directory.
    """
    print("Cleaning build artifacts...")

    # Patterns for files to be removed, covering common LaTeX temporary files,
    # generated TeX files, and the final PDF output.
    patterns = [
        "*.aux",
        "*.log",
        "*.out",
        "*.toc",
        "pycpbook.pdf",  # Target the specific PDF name
        "*.fls",
        "*.fdb_latexmk",
        "_generated_*.tex",
    ]

    root_dir = os.path.dirname(os.path.abspath(__file__))
    files_removed_count = 0

    # Clean from the root directory
    for pattern in patterns:
        for file_path in glob.glob(os.path.join(root_dir, pattern)):
            try:
                os.remove(file_path)
                print(f"Removed: {os.path.basename(file_path)}")
                files_removed_count += 1
            except OSError as e:
                print(f"Error removing file {file_path}: {e}", file=sys.stderr)

    # Clean from the content directory as pdflatex runs there
    content_dir = os.path.join(root_dir, "content")
    for pattern in patterns:
        for file_path in glob.glob(os.path.join(content_dir, pattern)):
            try:
                os.remove(file_path)
                print(f"Removed: {os.path.basename(file_path)}")
                files_removed_count += 1
            except OSError as e:
                print(f"Error removing file {file_path}: {e}", file=sys.stderr)

    # The 'minted' package creates a _minted* directory for cached code highlighting.
    # This should also be removed. It can be created in root or content.
    minted_dirs = glob.glob(os.path.join(root_dir, "**/_minted*", recursive=True))
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

    # 1. Verify pdflatex dependency is met
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

    # 2. Scan content directories (chapters)
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

        # 3. Process each Python file in the chapter
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

            # Use AST to safely parse the file
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

            # 4. Generate the intermediate .tex file
            with open(generated_tex_path, "w", encoding="utf-8") as tex_file:
                # Add a section title from the filename
                section_title = base_filename.replace("_", " ").title()
                tex_file.write(f"\\subsection*{{{section_title}}}\n\n")

                # Write the docstring inside its custom environment
                if docstring:
                    escaped_docstring = _escape_latex(docstring)
                    tex_file.write("\\begin{docstring}\n")
                    tex_file.write(escaped_docstring)
                    tex_file.write("\n\\end{docstring}\n\n")

                # Write the source code inside a minted block
                tex_file.write("\\begin{minted}{python}\n")
                tex_file.write(source_code)
                tex_file.write("\n\\end{minted}\n")

        # 5. Update the chapter's main .tex file to include generated files
        chapter_tex_path = os.path.join(chapter_path, "chapter.tex")
        with open(chapter_tex_path, "w", encoding="utf-8") as f:
            f.write("% This file is automatically generated by build.py.\n")
            f.write("% Do not edit manually.\n\n")
            for generated_file in generated_tex_files:
                f.write(f"\\input{{{os.path.join(chapter, generated_file)}}}\n")

    # 6. Compile the PDF using pdflatex
    print("\nCompiling LaTeX document...")
    main_tex_file = "pycpbook.tex"
    # The minted package requires '--shell-escape' to be enabled.
    # '-interaction=nonstopmode' prevents the compiler from stopping on errors.
    pdflatex_command = [
        "pdflatex",
        "--shell-escape",
        "-interaction=nonstopmode",
        main_tex_file,
    ]

    for i in range(2):  # Run twice for ToC and references
        print(f"--- Pass {i + 1} ---")
        try:
            # We run the command from within the 'content' directory so that
            # LaTeX can find the input files easily.
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
                    # Print the last 20 lines of the log for quick diagnosis
                    log_lines = f.readlines()
                    print("\n--- Last 20 lines of log file ---\n", file=sys.stderr)
                    sys.stderr.writelines(log_lines[-20:])
            sys.exit(1)

    # 7. Move the final PDF to the project root
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
    Discovers and runs all stress tests located in the 'stress-tests/' directory.

    The script recursively scans for Python files, excluding the 'utilities/'
    subdirectory. Each found test script is executed as a separate process.
    If any test script exits with a non-zero status code, this function
    will report the failure and terminate the build script, ensuring CI/CD
    workflows correctly identify test failures.
    """
    print("Running all stress tests...")

    root_dir = os.path.dirname(os.path.abspath(__file__))
    tests_dir = os.path.join(root_dir, "stress-tests")
    utilities_dir = os.path.join(tests_dir, "utilities")

    test_files = []
    # Find all Python files recursively in the stress-tests directory.
    for file_path in glob.glob(os.path.join(tests_dir, "**", "*.py"), recursive=True):
        # Exclude files in the utilities subdirectory.
        # This check works by seeing if the utilities path is a parent of the file path.
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
            # Execute the test script using the same Python interpreter.
            # 'check=True' will raise CalledProcessError on a non-zero exit code.
            # 'capture_output=True' and 'text=True' capture stdout/stderr as strings.
            result = subprocess.run(
                [sys.executable, test_file],
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            # Print test output only if it's not empty, to keep the log clean.
            if result.stdout.strip():
                print(result.stdout)
            print(f"--- PASS: {relative_path} ---\n")
        except subprocess.CalledProcessError as e:
            # This block executes if the test script fails (e.g., an assertion fails).
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
        # Exit with a non-zero status code to signal failure to CI systems.
        sys.exit(1)
    else:
        print(f"\nSummary: All {len(test_files)} tests passed successfully!")


def main():
    """
    The main entry point for the script.
    It sets up the command-line argument parser and executes the function
    associated with the chosen command.
    """
    parser = argparse.ArgumentParser(
        description="Build and utility script for the Python Competitive Programming Notebook (PyCPBook)."
    )
    # Using subparsers to create distinct commands like 'git push', 'git pull'.
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    # Subparser for the 'pdf' command.
    pdf_parser = subparsers.add_parser(
        "pdf", help="Parse content and generate the PDF notebook."
    )
    pdf_parser.set_defaults(func=run_pdf)

    # Subparser for the 'test' command.
    test_parser = subparsers.add_parser(
        "test", help="Discover and run all stress tests."
    )
    test_parser.set_defaults(func=run_test)

    # Subparser for the 'clean' command.
    clean_parser = subparsers.add_parser(
        "clean", help="Clean up all build artifacts and temporary files."
    )
    clean_parser.set_defaults(func=run_clean)

    args = parser.parse_args()
    # Execute the function that was associated with the chosen subparser.
    args.func()


if __name__ == "__main__":
    main()
