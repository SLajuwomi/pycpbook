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
    Placeholder function for the stress testing command.
    Full implementation will be handled in a future step.
    """
    print("Stress test execution is not yet implemented.")
    # The full logic will involve:
    # 1. Scanning the 'stress-tests/' directory for test scripts.
    # 2. Executing each script using 'subprocess'.
    # 3. Reporting any failures.


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
