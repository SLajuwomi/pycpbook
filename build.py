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
- A TeX distribution (for the 'pdf' command, to be fully implemented later).
"""

import argparse
import glob
import os
import shutil
import subprocess
import sys


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
        "*.pdf",
        "*.fls",
        "*.fdb_latexmk",
        "_generated_*.tex",
    ]

    root_dir = os.path.dirname(os.path.abspath(__file__))
    files_removed_count = 0

    for pattern in patterns:
        # Search for files matching the pattern in the project's root directory.
        for file_path in glob.glob(os.path.join(root_dir, pattern)):
            try:
                os.remove(file_path)
                print(f"Removed: {os.path.basename(file_path)}")
                files_removed_count += 1
            except OSError as e:
                print(f"Error removing file {file_path}: {e}", file=sys.stderr)

    # The 'minted' package creates a _minted* directory for cached code highlighting.
    # This should also be removed.
    minted_dirs = glob.glob(os.path.join(root_dir, "_minted*"))
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
    Placeholder function for the PDF generation command.
    Full implementation will be handled in a future step.
    """
    print("PDF generation is not yet implemented.")
    # The full logic will involve:
    # 1. Scanning the 'content/' directory.
    # 2. Parsing Python files to extract docstrings and code.
    # 3. Generating intermediate .tex files.
    # 4. Calling 'pdflatex' to compile the final PDF.


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
