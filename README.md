# Python Competitive Programming Notebook (PyCPBook)

PyCPBook is a comprehensive, high-quality competitive programming reference and learning document for Python, inspired by KTH's KACTL. The project includes a library of well-tested, copy-pasteable Python code snippets for common algorithms and data structures, accompanied by detailed explanations to make it accessible for learners. It features an automated build system to generate a printable PDF version using LaTeX.

## Setup

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/pycpbook.git](https://github.com/your-username/pycpbook.git)
    cd pycpbook
    ```

2.  **Install dependencies:**

    - A **Python 3.8+** interpreter is required.
    - A **TeX distribution** (like TeX Live, MiKTeX, or MacTeX) is required to build the PDF. Ensure the `pdflatex` command is available in your system's `PATH`.

3.  **(Optional) Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

## Usage

The project is managed via the `build.py` script.

- **Build the PDF:**

  ```bash
  python build.py pdf
  ```

  This command will parse all the content, generate the necessary LaTeX files, and compile them into `pycpbook.pdf` in the root directory.

- **Run all stress tests:**

  ```bash
  python build.py test
  ```

  This command will discover and execute all stress tests located in the `stress-tests/` directory to verify the correctness of the algorithms.

- **Clean build artifacts:**
  ```bash
  python build.py clean
  ```
  This command will remove all temporary files generated during the LaTeX build process (e.g., `.aux`, `.log`) and the final PDF.
