# Python Competitive Programming Notebook (PyCPBook)

**PyCPBook** is a comprehensive, open-source competitive programming reference for Python, inspired by the legendary KTH `KACTL`. It provides a curated library of high-quality, stress-tested, and performance-optimized code snippets for common algorithms and data structures. Each snippet is accompanied by a detailed explanation, making it an ideal resource for both learning and contest preparation.

The entire notebook is automatically compiled into a clean, printable, multi-column PDF using a LaTeX-based build system.

![CI](https://github.com/slajuwomi/pycpbook/actions/workflows/ci.yml/badge.svg)

## Features

- **Comprehensive Content**: Covers a wide range of topics from basic data structures to advanced algorithms in graph theory, string processing, number theory, geometry, and dynamic programming.
- **High-Quality Code**: All implementations are clean, concise, and optimized for performance in a competitive programming environment.
- **Thorough Explanations**: Each code snippet includes a detailed docstring explaining the underlying algorithm, its complexity, and usage.
- **Rigorously Tested**: Every single algorithm is validated by a corresponding stress test against a naive or known-correct implementation, ensuring reliability under pressure.
- **Automated PDF Generation**: A single command builds the entire notebook into a beautifully formatted, portable PDF document.
- **CI Integrated**: Continuous integration with GitHub Actions automatically runs all stress tests on every push, guaranteeing the correctness of the library.

## Setup

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/slajuwomi/pycpbook.git
    cd pycpbook
    ```

2.  **Install Dependencies:**

    - A **Python 3.8+** interpreter is required.
    - A **TeX distribution** (like TeX Live, MiKTeX, or MacTeX) is required to build the PDF. Ensure the `pdflatex` command is available in your system's `PATH`.

3.  **(Optional) Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

## Usage

The project is managed via the `build.py` script.

- **Build the PDF:**
  This command parses all content, generates the necessary LaTeX files, and compiles them into `pycpbook.pdf` in the root directory.

  ```bash
  python build.py pdf
  ```

- **Run All Stress Tests:**
  This command discovers and executes all stress tests located in the `stress_tests/` directory to verify the correctness of the algorithms.

  ```bash
  python build.py test
  ```

- **Clean Build Artifacts:**
  This command removes all temporary files generated during the LaTeX build process (e.g., `.aux`, `.log`) and the final PDF.

  ```bash
  python build.py clean
  ```

## Project Structure

The repository is organized to separate content, tests, and build-related files.

```
.
├── .github/              # GitHub Actions CI configuration.
├── content/              # Source code and explanations for the notebook.
├── doc/                  # LaTeX styling and preamble.
├── stress_tests/         # Validation scripts for all algorithms.
├── README.md             # This file.
└── build.py              # Main build and utility script.
```

## Contributing

Contributions are welcome! If you'd like to add a new algorithm or improve an existing one, please follow these steps:

1.  **Fork the repository.**
2.  **Create a new branch** for your feature (`git checkout -b feature/new-algorithm`).
3.  **Add your content:**
    - Place your new algorithm in the appropriate subdirectory within `content/` (e.g., `content/graph/new_algorithm.py`).
    - Follow the standardized docstring format for explanations and metadata.
4.  **Add a stress test:**
    - Create a corresponding test file in `stress_tests/` (e.g., `stress_tests/graph/new_algorithm.py`).
    - The test must validate your implementation against a naive or known-correct solution using randomized inputs.
5.  **Verify your changes:**
    - Run `python build.py test` to ensure all tests, including yours, pass.
    - Run `python build.py pdf` to confirm that the document builds successfully with your new content.
6.  **Commit your changes and open a pull request.**
