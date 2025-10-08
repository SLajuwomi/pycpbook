
You are an AI code generator responsible for implementing a web application based on a provided technical specification and implementation plan.

Your task is to systematically implement each step of the plan, one at a time.

First, carefully review the following inputs:

<existing_code>



</existing_code>

<project_request>

# Project Name

Python Competitive Programming Notebook (PyCPBook)

## Project Description

To create a comprehensive, high-quality competitive programming reference and learning document for Python, inspired by KTH's KACTL. The project will include a library of well-tested, copy-pasteable Python code snippets for common algorithms and data structures, accompanied by detailed explanations to make it accessible for learners. It will feature an automated build system to generate a printable PDF version using LaTeX. This document serves as the complete specification for the project.

## Project Structure

- [ ]  The project will be organized into the following top-level directories:
    - [ ]  **`content/`**: Contains the Python source code and LaTeX chapter files, organized by topic.
    - [ ]  **`stress-tests/`**: Contains corresponding stress tests for the code in `content/`.
    - [ ]  **`doc/`**: Contains build scripts, LaTeX styling, and other documentation.
    - [ ]  **`.github/`**: Contains CI/CD workflows, like GitHub Actions.

## Target Audience

- [ ]  Competitive programmers of all skill levels (Beginner, Intermediate, Advanced). The resource will serve both as a learning tool and a reliable contest reference.

## Desired Features

### Core Content

- [ ]  Cover standard competitive programming topics in a structured manner. Each topic below represents a required chapter in the notebook.
    - [ ]  **Contest & Setup**:
        - [ ]  Standard `template.py`.
        - [ ]  Fast I/O implementation and usage.
        - [ ]  Common debugging techniques and tricks.
        - [ ]  Python-specific optimizations.
    - [ ]  **Data Structures**:
        - [ ]  Fenwick Tree (1D and 2D).
        - [ ]  Segment Tree (with lazy propagation).
        - [ ]  Union-Find / Disjoint Set Union (with path compression and union by size/rank).
        - [ ]  Sparse Table / RMQ.
        - [ ]  Balanced Binary Search Tree (e.g., Treap).
        - [ ]  Hash Map (and notes on custom hashing to prevent collisions).
        - [ ]  Ordered Set (using a balanced BST).
        - [ ]  Line Container (for convex hull trick).
    - [ ]  **Graph Algorithms**:
        - [ ]  Graph Traversal (BFS, DFS).
        - [ ]  Topological Sort.
        - [ ]  Shortest Paths (Dijkstra, Bellman-Ford, Floyd-Warshall).
        - [ ]  Minimum Spanning Tree (Prim's, Kruskal's).
        - [ ]  Strongly Connected Components (Tarjan's or Kosaraju's).
        - [ ]  2-SAT.
        - [ ]  Maximum Flow (Dinic's algorithm).
        - [ ]  Bipartite Matching (Hopcroft-Karp or augmenting paths).
        - [ ]  Lowest Common Ancestor (Binary Lifting).
        - [ ]  Euler Path/Cycle.
    - [ ]  **String Algorithms**:
        - [ ]  String Hashing (Polynomial Hashing).
        - [ ]  Knuth-Morris-Pratt (KMP).
        - [ ]  Z-Algorithm.
        - [ ]  Suffix Array and LCP Array.
        - [ ]  Aho-Corasick.
        - [ ]  Manacher's Algorithm.
    - [ ]  **Mathematics & Number Theory**:
        - [ ]  Modular Arithmetic (inverse, power).
        - [ ]  Extended Euclidean Algorithm.
        - [ ]  Chinese Remainder Theorem.
        - [ ]  Primality Testing (Miller-Rabin).
        - [ ]  Integer Factorization (Pollard's Rho).
        - [ ]  Sieve of Eratosthenes.
        - [ ]  Fast Fourier Transform / Number Theoretic Transform for polynomial multiplication.
    - [ ]  **Geometry**:
        - [ ]  Foundational `Point` class with vector operations.
        - [ ]  Basic Primitives: dot/cross product, distance, orientation tests.
        - [ ]  Convex Hull (Graham Scan or Monotone Chain).
        - [ ]  Line/Segment Intersection.
        - [ ]  Polygon Area and Centroid.
    - [ ]  **Dynamic Programming**:
        - [ ]  Common DP patterns (e.g., LIS, LCS, Knapsack).
        - [ ]  DP optimizations: Knuth-Yao, Divide and Conquer DP, Convex Hull Trick.

### Code Library

- [ ]  All code snippets will be written in Python 3.8+.
- [ ]  Code style will be a balance between PEP 8 and competitive programming brevity. File and function names will use `snake_case`.
- [ ]  No type hints will be used in the code snippets.
- [ ]  Each snippet will have a standardized docstring for metadata:
    
    ```python
    """
    Author: [Name]
    Source: [Origin, e.g., KACTL, TopCoder]
    Description: [Step-by-step explanation of the algorithm.]
    Time: [Complexity]
    Space: [Complexity]
    Status: [Stress-tested]
    """
    
    ```
    
- [ ]  A `template.py` will be provided, including common imports, fast I/O, and an increased recursion limit.
- [ ]  Foundational modules (e.g., `content/geometry/point.py`) will be used for consistency where appropriate.

### PDF Generation

- [ ]  Use LaTeX to generate a high-quality, printable PDF document.
- [ ]  The LaTeX structure will be modular (`main.tex`, `chapter.tex` files).
- [ ]  The build process will be automated via a Python script (`build.py`), which will parse docstrings and code from `.py` files and inject them into LaTeX `listings` with Python syntax highlighting.
- [ ]  The build script must accept commands: `python build.py pdf`, `python build.py test`, and `python build.py clean`.

### Testing Framework

- [ ]  A `stress-tests/` directory will contain validation scripts.
- [ ]  Every algorithm/data structure **must** be accompanied by a corresponding stress test.
- [ ]  Each test file will be self-contained, including a random data generator, a naive (brute-force) solution, and a comparison loop that asserts correctness.
- [ ]  Tests must be runnable via a single command and integrated with a CI service (GitHub Actions).

## Design Requests

- [ ]  The final PDF will have a clean, dense, multi-column layout.
- [ ]  The layout will effectively balance code snippets with their corresponding textual explanations.
- [ ]  The PDF will feature a table of contents and page headers for easy navigation.

## Other Notes

- [ ]  All fundamental algorithms (e.g., BFS, DFS, Dijkstra) must be included to make the notebook self-contained.
- [ ]  The project must be hosted on a Git repository.
- [ ]  A development process should be followed where each new feature consists of a code snippet, its docstring-based explanation, and a passing stress test before it is considered complete.

</project_request>

<project_rules>

### Project Rules for PyCPBook

These rules establish the guiding principles for the development of the PyCPBook. They are designed to ensure the final product is thorough, reliable, and expertly crafted for its target audience.

1. **Rigor and Thoroughness**
    - Every topic and sub-topic defined in the project request must be covered in detail. Do not take shortcuts or omit content due to perceived simplicity or complexity.
    - Explanations must be comprehensive and clear, breaking down algorithms step-by-step. The goal is to be a learning resource, not just a reference. Assume the user is intelligent but may not be familiar with the specific topic.
2. **Code Quality and Correctness**
    - All code must be double-checked for correctness, edge cases, and clarity before finalization.
    - The implementation must be robust and reliable, suitable for copy-pasting directly into a contest environment without modification.
    - Adopt the mindset of a senior Python engineer: write code that is not just functional, but also clean and maintainable within the project's style guidelines.
3. **Adherence to Competitive Programming Constraints**
    - Every line of code must be written with the typical constraints of a programming contest in mind.
    - **Time Complexity:** Prioritize implementations with the best asymptotic time complexity. Be mindful of constant factors and avoid Python features known to be slow (e.g., unnecessary object creation in tight loops).
    - **Memory Complexity:** Ensure solutions are memory-efficient.
    - **Implementation Speed:** Code should be concise and easy to type or adapt under time pressure.
4. **Python Best Practices (Adapted)**
    - Adhere to standard Python conventions (`snake_case` for files and functions) to maintain a professional and consistent codebase.
    - While following Pythonic principles, deviate where necessary for performance (e.g., using array indices over iterators in performance-critical sections).
5. **Separation of Concerns: Code vs. Explanation**
    - **Explanations belong in the docstring.** The detailed, step-by-step descriptions and complexity analyses must be written in the standardized docstring at the top of each file.
    - **Code should be clean.** ADD ABSOLUTELY NO INLINE COMMENTS IN THE CODE for explaining algorithmic steps. The code itself should be clear to an experienced programmer. ADD NO INLINE COMMENTS AT ALL!
6. **Comprehensive and Self-Contained Testing**
    - Every single algorithm and data structure snippet must have a corresponding stress test file. There are no exceptions.
    - Each test must be thorough, validating correctness against a naive, brute-force, or otherwise known-correct implementation using a wide range of randomly generated test cases. This includes handling edge cases like empty inputs, small N, and large values.
7. **Escape Backslashes:** All single backslashes (`\\`) in LaTeX commands must be escaped with another backslash to prevent Python `SyntaxWarning`s.
    - **Correct:** `Time: $O(\\\\log N)$`
    - **Incorrect:** `Time: $O(\\log N)$`**Math Expressions:** Use standard LaTeX math mode with `$...$` delimiters for complexities, variables, and formulas. The build system is designed to recognize and correctly render these expressions.
    - **Example:** `The complexity is $O(\\\\alpha(N))$ for $N$ elements.`**Inline Code:** Use backticks (``...``) for inline variable names, function names, or short code snippets within explanatory text. The build system will automatically render this content in a monospaced font.
    - **Example:** `The` solve()`function uses the`sys.stdin.readline() `method.`
    - To display a literal backslash inside a code snippet, use a double backslash (`\\\\`). For instance, to show the text `\\n`, you must write ``\\\\n`` in the docstring.
    Comprehensive and Self-Contained TestingEvery single algorithm and data structure snippet must have a corresponding stress test file. There are no exceptions.
    Each test must be thorough, validating correctness against a naive, brute-force, or otherwise known-correct implementation using a wide range of randomly generated test cases. This includes handling edge cases like empty inputs, small N, and large values.

---

</project_rules>

<technical_specification>

# Python Competitive Programming Notebook (PyCPBook) Technical Specification

## 1. System Overview

### Core Purpose and Value Proposition

The Python Competitive Programming Notebook (PyCPBook) is a comprehensive, open-source project designed to be the definitive reference and learning guide for competitive programming in Python. It provides a curated library of high-quality, stress-tested, and performance-optimized code snippets for common algorithms and data structures. The final output is a printable, beautifully formatted PDF generated via a fully automated LaTeX build system, inspired by KTH's KACTL.

### Key Workflows

1. **Content Development**: A contributor adds an algorithm by creating a `.py` source file with a standardized docstring, implementing the code, and providing a corresponding stress test file that validates its correctness against a naive solution.
2. **PDF Generation**: The `build.py` script automatically discovers all content files, parses the docstrings (explanations) and code, injects them into a LaTeX template structure, and compiles the final `pycpbook.pdf`.
3. **Continuous Integration**: Upon every code push, a GitHub Actions workflow automatically executes all stress tests, guaranteeing that the codebase remains correct and reliable.

### System Architecture

The system is a command-line-driven static site generator, where the "site" is a PDF document. The architecture is file-based, with no databases or servers.

Data Flow Diagram:

[Python Source Files (.py) in content/] -> [build.py Script (Parse & Generate)] -> [Intermediate LaTeX Files (.tex)] -> [pdflatex Compiler] -> [Final PDF (pycpbook.pdf)]

---

## 2. Project Structure

The project will adhere to the following directory and file structure. All file and directory names must be `snake_case`.

`pycpbook/
├── README.md               # Project overview, setup, and contribution guide.
├── build.py                # Main Python build script for PDF generation and testing.
├── .gitignore              # Standard Python gitignore.
│
├── content/                # All source code and LaTeX chapter files.
│   ├── pycpbook.tex        # Main LaTeX file that assembles the document.
│   │
│   ├── contest/
│   │   ├── chapter.tex
│   │   ├── template.py
│   │   └── debugging_tricks.py
│   │
│   ├── data_structures/
│   │   ├── chapter.tex
│   │   ├── fenwick_tree.py
│   │   ├── fenwick_tree_2d.py
│   │   ├── segment_tree_lazy.py
│   │   ├── union_find.py
│   │   ├── sparse_table.py
│   │   ├── treap.py
│   │   ├── hash_map_custom.py
│   │   ├── ordered_set.py
│   │   └── line_container.py
│   │
│   ├── graph/
│   │   ├── chapter.tex
│   │   ├── traversal.py         # Contains both BFS and DFS.
│   │   ├── topological_sort.py
│   │   ├── dijkstra.py
│   │   ├── bellman_ford.py
│   │   ├── floyd_warshall.py
│   │   ├── prim_kruskal.py      # Contains both Prim's and Kruskal's.
│   │   ├── scc.py               # Tarjan's or Kosaraju's.
│   │   ├── two_sat.py
│   │   ├── dinic.py             # Max Flow.
│   │   ├── bipartite_matching.py
│   │   ├── lca_binary_lifting.py
│   │   └── euler_path.py
│   │
│   ├── string/
│   │   ├── chapter.tex
│   │   ├── polynomial_hashing.py
│   │   ├── kmp.py
│   │   ├── z_algorithm.py
│   ... (and so on for all other required chapters: math, geometry, dp)
│
├── stress-tests/           # Validation scripts for all content algorithms.
│   ├── data_structures/
│   │   ├── fenwick_tree.py
│   │   └── ...
│   ├── graph/
│   │   └── ...
│   ├── utilities/            # Reusable helper modules for testing.
│   │   ├── random_gen.py     # Advanced random data generation helpers.
│   │   ├── graph_gen.py      # Random graph generation (trees, DAGs, general graphs).
│   │   └── polygon_gen.py    # Random polygon generation.
│
├── doc/
│   └── tex/
│       ├── pycpbook.sty      # Custom LaTeX styling (fonts, colors, layout).
│       └── preamble.tex      # LaTeX preamble, packages, and custom commands.
│
└── .github/
    └── workflows/
        └── ci.yml            # GitHub Actions CI configuration for running tests.`

---

## 3. Feature Specification

### 3.1 `build.py` Automation Script

- **User Story**: As a developer, I want a single command-line tool to build the PDF, run all tests, and clean the project directory so that the development process is simple and reproducible.
- **Implementation Steps**:
    1. **CLI Interface**: Use Python's `argparse` module to create three subcommands:
        - `python build.py pdf`: Triggers the PDF generation workflow.
        - `python build.py test`: Triggers the testing workflow.
        - `python build.py clean`: Removes temporary build files and the final PDF.
    2. **PDF Generation (`pdf` command)**:
        - The script will recursively scan the `content/` directory for subdirectories (chapters).
        - For each chapter, it will process all `.py` files.
        - For each `.py` file, it will open the file and read its content. It will use Python's `ast` module to safely parse the file and extract the top-level docstring.
        - The script will generate a corresponding `_generated_{filename}.tex` file. The docstring content is written as plain LaTeX text. The Python code is written inside a `\begin{lstlisting}[language=Python] ... \end{lstlisting}` block.
        - The `chapter.tex` file for each directory will be updated to `\input` all the `_generated_*.tex` files.
        - After all files are processed, the script will execute `pdflatex -interaction=nonstopmode pycpbook.tex` twice from the `content/` directory using the `subprocess` module.
    3. **Testing (`test` command)**:
        - The script will recursively scan the `stress-tests/` directory for all `.py` files, excluding the `utilities/` subdirectory.
        - It will execute each found test file as a separate process using `subprocess.run(['python', test_file_path], check=True)`.
        - If any test script exits with a non-zero status code, the main `build.py` script will terminate and report the failing test.
        - A summary of passed/failed tests will be printed to the console.
    4. **Cleanup (`clean` command)**:
        - The script will delete all files matching the patterns: `.aux`, `.log`, `.out`, `.toc`, `_generated_*.tex`, and `pycpbook.pdf`.
- **Error Handling**:
    - If `pdflatex` is not found in the system's PATH, the script will exit with an informative error message.
    - If a Python source file does not contain a docstring, a warning will be issued, but the build will proceed (only including the code).

### 3.2 Content Module and Docstring Standard

- **User Story**: As a user of the notebook, I want every code snippet to be accompanied by a clear, standardized explanation of what it does, its performance characteristics, and where it came from.
- **Implementation Steps**:
    1. **File Naming**: All files must be `snake_case.py`.
    2. **Code Style**: Code will be Python 3.8+. It will balance PEP 8 with the conciseness required for competitive programming (e.g., shorter variable names like `adj` for an adjacency list are acceptable). No type hints.
    3. **Standardized Docstring**: Every `.py` file in `content/` **must** begin with a multiline string docstring with the following structure. The build script will parse this exact structure.Python
        
        # 
        
        `"""
        Author: [Contributor Name]
        Source: [Origin, e.g., KACTL, USACO Guide, Self]
        Description: [A clear, step-by-step explanation of the algorithm or data structure. This can be multiple paragraphs long and should be detailed enough for someone to learn the concept from scratch. It should explain the 'why' behind the code.]
        Time: [Asymptotic time complexity, e.g., O(N log N)]
        Space: [Asymptotic space complexity, e.g., O(N)]
        Status: [Stress-tested]
        """`
        
- **Edge Cases**: The parsing logic in `build.py` must correctly handle multiline descriptions and complexities.

### 3.3 Stress Testing Framework

- **User Story**: As a developer, I want to be confident that every algorithm in the notebook is correct, so I need a rigorous and standardized way to test them against a wide range of inputs.
- **Implementation Steps**:
    1. **Parallel Structure**: For every `content/topic/algorithm.py`, there must exist a `stress-tests/topic/algorithm.py`.
    2. **Test File Structure**: Each test file must be a self-contained, executable script and follow this template:
        - Import the optimized solution from the `content` directory.
        - Import necessary testing utilities (e.g., `random`).
        - Define a `solve_naive(...)` function that implements a simple, brute-force, or otherwise known-correct solution.
        - Define a `generate_random_case()` function that produces valid, randomized inputs for the problem. This generator must include edge cases (e.g., empty inputs, small N, large N, values at boundaries).
        - A main execution block that runs a loop (e.g., for 1000 iterations). In each iteration, it:
            - Calls `generate_random_case()`.
            - Calls the optimized solution.
            - Calls the naive solution.
            - Asserts that the results are identical. If not, print the failing test case and exit with an error code.
        - If the loop completes, print a "Passed!" message and exit successfully.
- **Error Handling**: If an assertion fails, the script must print the inputs that caused the failure to standard error before exiting.

### 3.4 Continuous Integration (CI) Pipeline

- **User Story**: As a maintainer, I want to automatically verify that all code changes are correct and do not break existing functionality before they are merged.
- **Implementation (`.github/workflows/ci.yml`)**:YAML
    
    # 
    
    `name: CI
    
    on: [push, pull_request]
    
    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v3
        - name: Set up Python 3.10
          uses: actions/setup-python@v3
          with:
            python-version: '3.10'
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            # No external dependencies needed for this project yet.
        - name: Run all stress tests
          run: python build.py test`
    

---

## 4. Database Schema

Not Applicable. This project is a static document generator and code library; it does not require a database.

---

## 5. Server Actions

Not Applicable. This project does not involve a server or server-side actions.

---

## 6. Design System (PDF LaTeX)

### 6.1 Visual Style

This section defines the visual style of the generated PDF, configured in `doc/tex/pycpbook.sty`.

- **Color Palette**:
    - `main_text`: `#000000` (Black)
    - `header_text`: `#444444` (Dark Gray)
    - `code_background`: `#F5F5F5` (Very Light Gray)
    - `code_keyword`: `#000080` (Navy)
    - `code_string`: `#A31515` (Brown)
    - `code_comment`: `#008000` (Green)
- **Typography**:
    - **Body Text**: Latin Modern Roman, 10pt.
    - **Headings**: Latin Modern Sans, bold, various sizes.
    - **Code**: Fira Code or another modern monospaced font with ligatures, 9pt.
- **Layout Principles**:
    - **Page Size**: A4.
    - **Margins**: Narrow (e.g., 1.5cm) to maximize content density.
    - **Columns**: Two-column layout using the `multicol` package.
    - **Code Blocks**: Code snippets will be enclosed in styled boxes (using `mdframed` or `tcolorbox`) to visually separate them from explanatory text. These boxes should be breakable across columns and pages.

### 6.2 Core Components

- **Header**: The page header will contain the current chapter title on the left and the page number on the right.
- **Table of Contents**: A hyperlinked table of contents will be automatically generated at the beginning of the document.
- **Syntax Highlighting**: Code listings will use the `listings` package, configured with the specified color palette for Python syntax.

---

## 7. Component Architecture

Not Applicable. This project does not have a UI component architecture.

---

## 8. Authentication & Authorization

Not Applicable. This project is an offline tool and does not involve users, accounts, or permissions.

---

## 9. Data Flow

The data flow is linear and occurs at build time.

1. **Input**: A collection of `.py` files in the `content/` directory. Each file is a data source containing two parts: documentation (docstring) and implementation (code).
2. **Processing**: The `build.py` script acts as the processor. It reads each `.py` file, separates the two data parts, and transforms them into a new format: LaTeX (`.tex`) files.
3. **Integration**: The main `pycpbook.tex` file integrates these generated `.tex` fragments.
4. **Output**: The `pdflatex` engine processes the integrated LaTeX source to produce the final `pycpbook.pdf`.

---

## 10. Stripe Integration

Not Applicable.

---

## 11. PostHog Analytics

Not Applicable.

---

## 12. Testing

The testing strategy is paramount to the project's success and reliability.

- **Philosophy**: Every single algorithm and data structure implementation in the `content/` directory must have 100% corresponding stress test coverage. There are no exceptions. The goal is to ensure that any code snippet can be copied from the notebook during a contest with a very high degree of confidence in its correctness.
- **Unit Tests**: Not applicable in the traditional sense. Stress tests serve as correctness tests.
- **End-to-End (e2e) Tests**: The closest equivalent is the full execution of the `python build.py pdf` command, which tests that the entire document can be compiled without LaTeX errors. This will be manually verified during development. The CI pipeline primarily focuses on correctness via stress tests.
- **Stress Test Implementation Example (`stress-tests/data_structures/fenwick_tree.py`)**:Python
    
    # 
    
    `import random
    import sys
    import os
    
    # Add content directory to path to import the solution
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../content/data_structures'))
    from fenwick_tree import FenwickTree
    
    # Naive solution for comparison
    class NaiveFenwickTree:
        def __init__(self, size):
            self.arr = [0] * size
    
        def add(self, idx, delta):
            self.arr[idx] += delta
    
        def query(self, right): # query prefix sum up to right-1
            return sum(self.arr[:right])
    
    def run_test():
        N = 1000 # Size of the array
        ITERATIONS = 5000 # Number of operations
    
        ft = FenwickTree(N)
        naive_ft = NaiveFenwickTree(N)
    
        for i in range(ITERATIONS):
            # 50% chance to add, 50% chance to query
            op_type = random.randint(0, 1)
    
            if op_type == 0: # Add operation
                idx = random.randint(0, N - 1)
                val = random.randint(-100, 100)
                ft.add(idx, val)
                naive_ft.add(idx, val)
            else: # Query operation
                idx = random.randint(1, N) # Query is on [0, idx)
                res_optimized = ft.query(idx)
                res_naive = naive_ft.query(idx)
    
                assert res_optimized == res_naive, \
                    f"Query failed at idx {idx}! Expected: {res_naive}, Got: {res_optimized}"
    
        print("Fenwick Tree: All tests passed!")
    
    if __name__ == "__main__":
        run_test()`
    

</technical_specification>

<implementation_plan>

# Implementation Plan

This plan outlines the step-by-step process for building the Python Competitive Programming Notebook (PyCPBook). The process starts with setting up the project structure and core build automation, followed by the iterative implementation of each content module, complete with its corresponding stress test.

## Phase 1: Project Scaffolding & CI Setup

This phase establishes the foundational directory structure, version control configuration, and the Continuous Integration pipeline.

- [x]  Step 1: Create Project Directory Structure
    - **Task**: Generate all the necessary directories and empty placeholder files as defined in the technical specification. This creates the skeleton of the project.
    - **Files**:
        - `pycpbook/` (and all subdirectories: `content/contest`, `content/data_structures`, etc.)
        - `content/pycpbook.tex`: Empty main LaTeX file.
        - `content/**/chapter.tex`: Empty chapter include files.
        - `doc/tex/pycpbook.sty`: Empty LaTeX style file.
        - `doc/tex/preamble.tex`: Empty LaTeX preamble file.
        - `.github/workflows/ci.yml`: Empty CI workflow file.
        - `stress-tests/utilities/random_gen.py`: Empty file.
        - `stress-tests/utilities/graph_gen.py`: Empty file.
        - `stress-tests/utilities/polygon_gen.py`: Empty file.
    - **Step Dependencies**: None.
- [x]  Step 2: Initialize Project Configuration Files
    - **Task**: Create the `.gitignore` file with standard Python exclusions and a `README.md` file with a basic project description and setup instructions.
    - **Files**:
        - `.gitignore`: Add entries for Python cache (`__pycache__/`), build artifacts (`.pdf`, `.log`, `.aux`, `_generated_*.tex`), and environment files (`.venv/`).
        - `README.md`: Add the project title, a brief description, and sections for "Setup" and "Usage".
    - **Step Dependencies**: Step 1.
- [x]  Step 3: Implement Continuous Integration Workflow
    - **Task**: Configure the GitHub Actions workflow in `ci.yml` to automatically run tests on every push and pull request. This workflow will check out the code, set up Python, and run the main test command.
    - **Files**:
        - `.github/workflows/ci.yml`: Implement the YAML configuration as specified in the technical docs, which calls `python build.py test`.
    - **Step Dependencies**: Step 1.

---

## Phase 2: Core Build System & LaTeX Foundation

This phase focuses on creating the `build.py` script, which is central to the project's automation, and setting up the LaTeX document structure.

- [x]  Step 4: Implement `build.py` CLI and `clean` Command
    - **Task**: Create the main `build.py` script. Implement the command-line interface using `argparse` to handle the `pdf`, `test`, and `clean` subcommands. Fully implement the logic for the `clean` command to remove build artifacts.
    - **Files**:
        - `build.py`: Set up `argparse`. Implement the function for the `clean` command, using `os` and `glob` to find and delete files like `.aux`, `.log`, `.pdf`, and `_generated_*.tex`.
    - **Step Dependencies**: Step 1.
- [x]  Step 5: Implement `test` Command in `build.py`
    - **Task**: Implement the logic for the `test` command. The script should recursively scan the `stress-tests/` directory (excluding `utilities/`), execute each found Python script using `subprocess.run`, and report any failures.
    - **Files**:
        - `build.py`: Add logic to the `test` command handler to discover and run test files, checking for non-zero exit codes.
    - **Step Dependencies**: Step 4.
- [x]  Step 6: Set Up LaTeX Document Structure and Styling
    - **Task**: Define the core LaTeX structure and styling for the PDF. This includes setting up the document class, packages, custom commands, colors, fonts, and page layout.
    - **Files**:
        - `doc/tex/preamble.tex`: Add common LaTeX `\usepackage` commands (e.g., `geometry`, `amsmath`, `graphicx`, `multicol`, `hyperref`, `listings`).
        - `doc/tex/pycpbook.sty`: Define custom colors, configure the `listings` package for Python syntax highlighting, set page geometry (A4, narrow margins), and define heading styles.
        - `content/pycpbook.tex`: Set up the main document environment. Input the `preamble.tex` and `pycpbook.sty`. Add title, author, table of contents, and a structure to `\input` the `chapter.tex` files.
    - **Step Dependencies**: Step 1.
    - **User Instructions**: To build the PDF locally, you must have a TeX distribution (like TeX Live, MiKTeX, or MacTeX) installed on your system, and the `pdflatex` command must be available in your system's PATH.
- [x]  Step 7: Implement `pdf` Command in `build.py`
    - **Task**: Implement the core logic for the `pdf` command. This involves recursively scanning `content/`, parsing each `.py` file to separate the docstring from the code using the `ast` module, generating temporary `_generated_{filename}.tex` files, and finally compiling the PDF using `subprocess.run` to call `pdflatex`.
    - **Files**:
        - `build.py`: Implement the `pdf` command handler with file scanning, `ast` parsing, `.tex` file generation, and calls to `pdflatex`.
        - `content/**/chapter.tex`: Add a placeholder comment indicating where generated files will be input. The build script will dynamically manage the `\input` commands.
    - **Step Dependencies**: Step 5, Step 6.

## Phase 3: Foundational Content & Testing Utilities

With the build system in place, this phase adds the first pieces of content and the necessary utilities for writing comprehensive stress tests.

- [x]  Step 8: Create Stress Test Utility Modules
    - **Task**: Implement helper functions in the `utilities/` directory to facilitate the creation of complex random test cases for data structures, graphs, and geometry problems.
    - **Files**:
        - `stress-tests/utilities/random_gen.py`: Add helpers for generating random lists, numbers within a range, etc.
        - `stress-tests/utilities/graph_gen.py`: Add functions to generate random trees, DAGs, and general graphs with `N` nodes and `M` edges.
        - `stress-tests/utilities/polygon_gen.py`: Add a function to generate random simple polygons.
    - **Step Dependencies**: Step 1.
- [x]  Step 9: Implement "Contest & Setup" Chapter Content
    - **Task**: Create the initial content for the "Contest & Setup" chapter. This includes the standard contest template and a file for debugging tricks. These are foundational elements for any competitive programmer.
    - **Files**:
        - `content/contest/template.py`: Create the template with fast I/O, common imports (`sys`, `os`, `math`), and an increased recursion limit. Add a complete docstring explaining its usage.
        - `content/contest/debugging_tricks.py`: Create a placeholder file with a docstring explaining that this section will contain notes on common debugging techniques.
    - **Step Dependencies**: Step 7.

---

## Phase 4: Data Structures Implementation

This phase involves the systematic implementation of each data structure, ensuring each is accompanied by a rigorous stress test.

- [x]  Step 10: Implement Union-Find Data Structure
    - **Task**: Implement the Disjoint Set Union (DSU) or Union-Find data structure with path compression and union by size/rank optimizations. Create a corresponding stress test to validate its correctness.
    - **Files**:
        - `content/data_structures/union_find.py`: Implement the `UnionFind` class and its methods (`find`, `union`). Write a detailed docstring explaining the algorithms and complexities.
        - `stress-tests/data_structures/union_find.py`: Write a test that compares the custom `UnionFind` implementation against a naive approach (e.g., using a simple list/dict) over thousands of random union and find operations.
    - **Step Dependencies**: Step 5, Step 8.
- [x]  Step 11: Implement Fenwick Tree (1D)
    - **Task**: Implement a 1D Fenwick Tree (Binary Indexed Tree) for prefix sum queries and point updates. Create a stress test comparing it against a naive array with prefix sums.
    - **Files**:
        - `content/data_structures/fenwick_tree.py`: Implement the `FenwickTree` class with `add` and `query` methods. Add a detailed docstring.
        - `stress-tests/data_structures/fenwick_tree.py`: Write a test that performs random updates and prefix sum queries, asserting correctness against a simple array.
    - **Step Dependencies**: Step 5, Step 8.
- [x]  Step 12: Implement Fenwick Tree (2D)
    - **Task**: Implement a 2D Fenwick Tree for 2D prefix sum queries and point updates. The stress test will compare it against a naive 2D prefix sum array.
    - **Files**:
        - `content/data_structures/fenwick_tree_2d.py`: Implement the 2D Fenwick Tree class.
        - `stress-tests/data_structures/fenwick_tree_2d.py`: Write a test performing random 2D updates and queries, validating against a naive solution.
    - **Step Dependencies**: Step 11.
- [x]  Step 13: Implement Segment Tree with Lazy Propagation
    - **Task**: Implement a Segment Tree supporting range queries and range updates with lazy propagation. The stress test will validate range sums/mins/maxes against a naive array.
    - **Files**:
        - `content/data_structures/segment_tree_lazy.py`: Implement the `SegmentTree` class, including `build`, `query`, `update`, and lazy propagation logic.
        - `stress-tests/data_structures/segment_tree_lazy.py`: Write a test performing random range updates and range queries, asserting correctness against a simple array modified with loops.
    - **Step Dependencies**: Step 5, Step 8.
- [x]  Step 14: Implement Sparse Table
    - **Task**: Implement a Sparse Table for fast Range Minimum/Maximum Query (RMQ). The stress test will verify its correctness against naive linear scans over ranges.
    - **Files**:
        - `content/data_structures/sparse_table.py`: Implement the `SparseTable` class for RMQ.
        - `stress-tests/data_structures/sparse_table.py`: Write a test that pre-builds the table and then performs thousands of random range queries, comparing with a simple `min()` on a slice.
    - **Step Dependencies**: Step 5, Step 8.
- [x]  Step 15: Implement Treap / Balanced BST
    - **Task**: Implement a Treap, a randomized balanced binary search tree, to support standard BST operations (insert, delete, search).
    - **Files**:
        - `content/data_structures/treap.py`: Implement the `Node` and `Treap` classes.
        - `stress-tests/data_structures/treap.py`: Write a test comparing Treap operations against a sorted list or Python's `bisect` module.
    - **Step Dependencies**: Step 5, Step 8.
- [x]  Step 16: Implement Ordered Set
    - **Task**: Implement an Ordered Set using the previously built Treap or another balanced BST. It should support finding the k-th smallest element and the rank of an element.
    - **Files**:
        - `content/data_structures/ordered_set.py`: Create a wrapper class or extend the Treap to support `find_by_order` and `order_of_key`.
        - `stress-tests/data_structures/ordered_set.py`: Write a test comparing the ordered set operations against a sorted list.
    - **Step Dependencies**: Step 15.
- [x]  Step 17: Implement Line Container (Convex Hull Trick)
    - **Task**: Implement a Line Container for the convex hull trick, supporting adding lines and querying for the minimum/maximum value at a point.
    - **Files**:
        - `content/data_structures/line_container.py`: Implement the Line Container structure.
        - `stress-tests/data_structures/line_container.py`: Write a test that adds random lines and queries points, comparing against a naive evaluation of all stored lines.
    - **Step Dependencies**: Step 5, Step 8.
- [x]  Step 18: Implement Custom Hash Map Notes
    - **Task**: Create a Python file explaining the concept of custom hashing in Python to prevent collisions in competitive programming, including a simple example.
    - **Files**:
        - `content/data_structures/hash_map_custom.py`: Add code for a custom hash class for use with Python dictionaries and a detailed docstring explaining anti-hash tests and techniques.
        - `stress-tests/data_structures/hash_map_custom.py`: A simple test demonstrating the usage of the custom hash.
    - **Step Dependencies**: Step 5.

## Phase 5: Graph Algorithms Implementation

This phase covers the implementation of fundamental and advanced graph algorithms.

- [x]  Step 19: Implement Graph Traversal (BFS & DFS)
    - **Task**: Implement both Breadth-First Search (BFS) and Depth-First Search (DFS) in a single file.
    - **Files**:
        - `content/graph/traversal.py`: Include functions for both `bfs` and `dfs`.
        - `stress-tests/graph/traversal.py`: Write a test that generates a random graph and verifies that all reachable nodes are visited by comparing the output with a simple iterative approach.
    - **Step Dependencies**: Step 8.
- [x]  Step 20: Implement Topological Sort
    - **Task**: Implement Topological Sort using Kahn's algorithm (BFS-based) or DFS-based approach.
    - **Files**:
        - `content/graph/topological_sort.py`: Implement the topological sort function.
        - `stress-tests/graph/topological_sort.py`: Write a test that generates a random Directed Acyclic Graph (DAG) and verifies that the output is a valid topological ordering.
    - **Step Dependencies**: Step 8, Step 19.
- [x]  Step 21: Implement Dijkstra's and Bellman-Ford's Algorithms
    - **Task**: Implement Dijkstra's algorithm for single-source shortest paths on graphs with non-negative edge weights and Bellman-Ford for graphs with negative weights.
    - **Files**:
        - `content/graph/dijkstra.py`: Implement Dijkstra's using a priority queue.
        - `stress-tests/graph/dijkstra.py`: Test against a BFS on an unweighted graph or a simpler shortest path algorithm on small graphs.
        - `content/graph/bellman_ford.py`: Implement Bellman-Ford, including negative cycle detection.
        - `stress-tests/graph/bellman_ford.py`: Test against a naive DP solution on small random graphs.
    - **Step Dependencies**: Step 8.
- [x]  Step 22: Implement Floyd-Warshall Algorithm
    - **Task**: Implement the Floyd-Warshall algorithm for all-pairs shortest paths.
    - **Files**:
        - `content/graph/floyd_warshall.py`: Implement the Floyd-Warshall algorithm.
        - `stress-tests/graph/floyd_warshall.py`: Test against running Dijkstra/Bellman-Ford from every node on small graphs.
    - **Step Dependencies**: Step 21.
- [x]  Step 23: Implement MST Algorithms (Prim's & Kruskal's)
    - **Task**: Implement both Prim's and Kruskal's algorithms for finding the Minimum Spanning Tree (MST) of a graph.
    - **Files**:
        - `content/graph/prim_kruskal.py`: Include implementations for both algorithms.
        - `stress-tests/graph/prim_kruskal.py`: Generate a random weighted graph and assert that both algorithms produce the same total MST weight.
    - **Step Dependencies**: Step 10 (for Kruskal's).
- [x]  Step 24: Implement Strongly Connected Components (SCC)
    - **Task**: Implement an algorithm to find SCCs, such as Tarjan's algorithm or Kosaraju's algorithm.
    - **Files**:
        - `content/graph/scc.py`: Implement the chosen SCC algorithm.
        - `stress-tests/graph/scc.py`: Write a test that generates a graph and verifies the SCC properties (e.g., all nodes in an SCC can reach each other).
    - **Step Dependencies**: Step 19.
- [x]  Step 25: Implement Maximum Flow (Dinic's Algorithm)
    - **Task**: Implement Dinic's algorithm for computing maximum flow in a flow network.
    - **Files**:
        - `content/graph/dinic.py`: Implement Dinic's algorithm.
        - `stress-tests/graph/dinic.py`: Test on small, hand-crafted networks or compare against a simpler max-flow algorithm like Edmonds-Karp.
    - **Step Dependencies**: Step 19.
- [x]  Step 26: Implement Lowest Common Ancestor (LCA)
    - **Task**: Implement LCA using the binary lifting technique.
    - **Files**:
        - `content/graph/lca_binary_lifting.py`: Implement the LCA precomputation and query logic.
        - `stress-tests/graph/lca_binary_lifting.py`: Generate a random tree, and for random pairs of nodes, find the LCA by binary lifting and by a naive path traversal upwards, then assert they are the same.
    - **Step Dependencies**: Step 8, Step 19.

## Phase 5: Graph Algorithms Implementation (Continued)

- [x]  Step 27: Implement 2-SAT
    - **Task**: Implement a solver for 2-satisfiability (2-SAT) problems by reducing it to a Strongly Connected Components problem on an implication graph.
    - **Files**:
        - `content/graph/two_sat.py`: Implement the `TwoSAT` solver class, which builds the implication graph and uses an SCC algorithm to find a solution.
        - `stress-tests/graph/two_sat.py`: Write a test that generates random 2-CNF formulas, solves them, and verifies the solution by plugging the variable assignments back into the original formula.
    - **Step Dependencies**: Step 24.
- [x]  Step 28: Implement Bipartite Matching
    - **Task**: Implement an algorithm for maximum bipartite matching, such as one based on augmenting paths (Ford-Fulkerson on a flow network) or the Hopcroft-Karp algorithm.
    - **Files**:
        - `content/graph/bipartite_matching.py`: Implement the maximum matching algorithm.
        - `stress-tests/graph/bipartite_matching.py`: Test against a max-flow implementation (like Dinic's) on the corresponding flow network, as max-flow equals max-matching in a bipartite graph.
    - **Step Dependencies**: Step 19, Step 25.
- [x]  Step 29: Implement Euler Path/Cycle
    - **Task**: Implement Hierholzer's algorithm to find an Euler path or cycle in a graph. The implementation should handle both directed and undirected graphs.
    - **Files**:
        - `content/graph/euler_path.py`: Implement the function to find an Euler path/cycle.
        - `stress-tests/graph/euler_path.py`: Write a test that generates a random Eulerian graph, finds the path, and verifies that it visits every edge exactly once.
    - **Step Dependencies**: Step 8.

---

## Phase 6: String Algorithms Implementation

This phase covers a suite of powerful algorithms for string processing and pattern matching.

- [x]  Step 30: Implement Polynomial Hashing
    - **Task**: Implement a string hashing class using polynomial rolling hash with a randomized base and multiple moduli to prevent collisions.
    - **Files**:
        - `content/string/polynomial_hashing.py`: Implement a `StringHasher` class that supports querying the hash of any substring in O(1) after precomputation.
        - `stress-tests/string/polynomial_hashing.py`: Write a test that compares hashes of random substrings against naively computed hashes to ensure correctness.
    - **Step Dependencies**: Step 5.
- [x]  Step 31: Implement Knuth-Morris-Pratt (KMP)
    - **Task**: Implement the KMP algorithm for efficient string searching, including the logic for building the prefix function (LPS array).
    - **Files**:
        - `content/string/kmp.py`: Implement the `compute_lps` and `kmp_search` functions.
        - `stress-tests/string/kmp.py`: Write a test that searches for random patterns in random text and compares the results with Python's built-in `string.find()` method.
    - **Step Dependencies**: Step 5.
- [x]  Step 32: Implement Z-Algorithm
    - **Task**: Implement the Z-algorithm to compute the Z-array (the length of the longest common prefix between a string and its suffixes).
    - **Files**:
        - `content/string/z_algorithm.py`: Implement the function to compute the Z-array.
        - `stress-tests/string/z_algorithm.py`: Write a test that computes the Z-array and verifies its values by naively comparing prefixes for random strings.
    - **Step Dependencies**: Step 5.
- [x]  Step 33: Implement Suffix Array and LCP Array
    - **Task**: Implement the construction of a Suffix Array and LCP (Longest Common Prefix) Array. A common approach is using sorting with a custom comparator or the SA-IS algorithm for O(N) complexity.
    - **Files**:
        - `content/string/suffix_array.py`: Implement the logic to build the suffix and LCP arrays.
        - `stress-tests/string/suffix_array.py`: Write a test that generates a random string, builds the suffix array, and asserts that the resulting suffixes are in lexicographically sorted order.
    - **Step Dependencies**: Step 5.
- [x]  Step 34: Implement Aho-Corasick Algorithm
    - **Task**: Implement the Aho-Corasick algorithm to find all occurrences of multiple patterns in a text simultaneously by building a trie with failure links.
    - **Files**:
        - `content/string/aho_corasick.py`: Implement the `AhoCorasick` class with methods to add patterns and search text.
        - `stress-tests/string/aho_corasick.py`: Write a test that searches for a set of patterns in a text and compares the findings against multiple runs of a naive search for each pattern.
    - **Step Dependencies**: Step 5.
- [x]  Step 35: Implement Manacher's Algorithm
    - **Task**: Implement Manacher's algorithm to find the longest palindromic substring in linear time.
    - **Files**:
        - `content/string/manacher.py`: Implement Manacher's algorithm.
        - `stress-tests/string/manacher.py`: Test by finding the longest palindrome and verifying its length and properties against a naive O(N^2) or O(N^3) check of all substrings.
    - **Step Dependencies**: Step 5.

---

## Phase 7: Mathematics & Number Theory Implementation

This phase covers essential mathematical tools for competitive programming.

- [x]  Step 36: Implement Modular Arithmetic Utilities
    - **Task**: Implement fundamental modular arithmetic operations: modular exponentiation (power) and modular inverse using Fermat's Little Theorem. Also, implement the Extended Euclidean Algorithm to find modular inverse for non-prime moduli.
    - **Files**:
        - `content/math/modular_arithmetic.py`: Include `power`, `mod_inverse`, and `extended_gcd` functions.
        - `stress-tests/math/modular_arithmetic.py`: Test `power` against `pow(a, b, m)`. Test `mod_inverse` by asserting that `(a * mod_inverse(a, m)) % m == 1`.
    - **Step Dependencies**: Step 5.
- [x]  Step 37: Implement Sieve of Eratosthenes
    - **Task**: Implement the Sieve of Eratosthenes to generate all prime numbers up to a given limit `N`.
    - **Files**:
        - `content/math/sieve.py`: Implement the sieve algorithm.
        - `stress-tests/math/sieve.py`: Test against a naive primality test function for all numbers up to a smaller limit (e.g., 1000) to verify the sieve's correctness.
    - **Step Dependencies**: Step 5.
- [x]  Step 38: Implement Primality Testing (Miller-Rabin)
    - **Task**: Implement the Miller-Rabin probabilistic primality test for efficiently checking if large numbers are prime.
    - **Files**:
        - `content/math/miller_rabin.py`: Implement the Miller-Rabin test.
        - `stress-tests/math/miller_rabin.py`: Test against the previously generated sieve for numbers within the sieve's range. Test with known large primes and composites.
    - **Step Dependencies**: Step 36, Step 37.
- [x]  Step 39: Implement Integer Factorization (Pollard's Rho)
    - **Task**: Implement Pollard's Rho algorithm for integer factorization, which is efficient for finding non-trivial factors of large composite numbers.
    - **Files**:
        - `content/math/pollard_rho.py`: Implement the Pollard's Rho algorithm, likely using Miller-Rabin for primality checks.
        - `stress-tests/math/pollard_rho.py`: Test by factoring random numbers and multiplying the factors back together to ensure they equal the original number.
    - **Step Dependencies**: Step 38.
- [x]  Step 40: Implement Chinese Remainder Theorem
    - **Task**: Implement a solver for a system of linear congruences using the Chinese Remainder Theorem (CRT).
    - **Files**:
        - `content/math/chinese_remainder_theorem.py`: Implement the CRT function.
        - `stress-tests/math/chinese_remainder_theorem.py`: Generate systems of congruences, solve for the unique solution, and verify that the solution satisfies all original congruences.
    - **Step Dependencies**: Step 36.
- [x]  Step 41: Implement FFT / NTT
    - **Task**: Implement Number Theoretic Transform (NTT) for fast polynomial multiplication over finite fields, which is often simpler and more practical in contests than a full floating-point FFT.
    - **Files**:
        - `content/math/ntt.py`: Implement the NTT algorithm and a `multiply` function for polynomials.
        - `stress-tests/math/ntt.py`: Test by multiplying random polynomials and comparing the result with a naive O(N^2) polynomial multiplication algorithm.
    - **Step Dependencies**: Step 36.

---

## Phase 8: Geometry Implementation

This phase builds the geometric primitives and algorithms.

- [x]  Step 42: Implement Foundational Point Class and Primitives
    - **Task**: Create a `Point` class with support for vector operations (addition, subtraction, scalar multiplication, dot/cross product, distance). Implement basic geometric primitives like orientation tests.
    - **Files**:
        - `content/geometry/point.py`: Define the `Point` class and its associated methods.
        - `stress-tests/geometry/point.py`: Write unit-style tests to verify each vector operation and primitive with known inputs and expected outputs.
    - **Step Dependencies**: Step 5.
- [x]  Step 43: Implement Line/Segment Intersection
    - **Task**: Implement functions to check for and find the intersection point of lines and line segments.
    - **Files**:
        - `content/geometry/line_intersection.py`: Implement the intersection logic.
        - `stress-tests/geometry/line_intersection.py`: Write tests with various cases: parallel lines, collinear lines, and standard intersections, asserting the results.
    - **Step Dependencies**: Step 42.
- [x]  Step 44: Implement Convex Hull
    - **Task**: Implement an algorithm for finding the convex hull of a set of points, such as Graham Scan or Monotone Chain.
    - **Files**:
        - `content/geometry/convex_hull.py`: Implement the convex hull algorithm.
        - `stress-tests/geometry/convex_hull.py`: Test against a naive O(N^3) algorithm on small sets of points, which checks every pair of points and sees if all other points lie on one side.
    - **Step Dependencies**: Step 42.
- [x]  Step 45: Implement Polygon Area and Centroid
    - **Task**: Implement functions to calculate the area of a simple polygon using the shoelace formula and to find its centroid.
    - **Files**:
        - `content/geometry/polygon_area.py`: Implement the area and centroid calculation functions.
        - `stress-tests/geometry/polygon_area.py`: Write tests with simple shapes (squares, triangles) where the area and centroid are known.
    - **Step Dependencies**: Step 42.

---

## Phase 9: Dynamic Programming Implementation

This phase covers common DP patterns and optimizations.

- [x]  Step 46: Implement Common DP Patterns
    - **Task**: Provide implementations for classic DP problems like Longest Increasing Subsequence (LIS) in O(N log N), Longest Common Subsequence (LCS), and Knapsack (0/1). These serve as templates for common patterns.
    - **Files**:
        - `content/dp/common_patterns.py`: Include well-documented functions for `lis`, `lcs`, and `knapsack`.
        - `stress-tests/dp/common_patterns.py`: Write validation tests for each function with specific test cases that have known, verifiable answers.
    - **Step Dependencies**: Step 5.
- [x]  Step 47: Implement DP Optimizations
    - **Task**: Create a file with implementations and/or detailed explanations of advanced DP optimizations, focusing on the Convex Hull Trick as it's the most common and implementable.
    - **Files**:
        - `content/dp/dp_optimizations.py`: Implement a clear example of the Convex Hull Trick, referencing the `LineContainer`. The docstring should explain Knuth-Yao and Divide & Conquer DP conceptually.
        - `stress-tests/dp/dp_optimizations.py`: Write a test that solves a problem amenable to CHT (e.g., from a known source like CSES) and validates its correctness against a simpler, slower DP solution.
    - **Step Dependencies**: Step 17, Step 46.

---

## Phase 10: Project Finalization

This final phase involves polishing the project for release.

- [x]  Step 48: Finalize Documentation and Build
    - **Task**: Thoroughly review and update the `README.md` with complete setup, usage, and contribution instructions. Perform a final build of the PDF to ensure all content is included, formatted correctly, and the table of contents is accurate.
    - **Files**:
        - `README.md`: Add detailed sections and examples for using `build.py`.
        - `content/pycpbook.tex`: Ensure all `chapter.tex` files are correctly included.
    - **Step Dependencies**: All previous steps.
    - **User Instructions**: Run `python build.py clean` followed by `python build.py pdf` one last time to generate the final `pycpbook.pdf` artifact.

## Phase 11: Foundational Content Implementation (New & Expanded)

This phase will add a new "Fundamentals" chapter to the notebook, covering core algorithmic techniques and Python-specific patterns essential for beginners.

- [x] Step 49: Create "Fundamentals" Chapter and Expanded Python Idioms Content
    - **Task**: Create the new directory structure for the "Fundamentals" chapter. Add the first content file, which will serve as a reference for powerful Python idioms, now including character and number conversion techniques.
    - **Files**:
        - `content/fundamentals/`: Create the new directory.
        - `content/fundamentals/chapter.tex`: Create the empty LaTeX chapter file.
        - `content/fundamentals/python_idioms.py`: Create the file with a detailed docstring and code examples for:
            - List/dict/set comprehensions.
            - Advanced sorting with lambda keys.
            - Common string manipulations (`split`, `join`, slicing).
            - **Character and number conversions** (`ord`, `chr`, `int`, `str`).
        - `stress-tests/fundamentals/`: Create the new directory.
        - `stress-tests/fundamentals/python_idioms.py`: Create a simple test script that executes all example snippets to ensure they are syntactically correct.
    - **Step Dependencies**: Phase 10.
- [x] Step 50: Implement Stacks and Queues Guide
    - **Task**: Add a content file that explicitly explains how to implement and use stacks and queues in Python.
    - **Files**:
        - `content/fundamentals/stacks_and_queues.py`: Create the file with examples for stacks (using `list`) and queues (using `collections.deque`). The docstring will explain LIFO vs. FIFO and the performance benefits of `deque` for queues.
        - `stress-tests/fundamentals/stacks_and_queues.py`: Create a simple demonstration script to validate the code examples.
    - **Step Dependencies**: Step 49.
- [x] Step 51: Implement Binary Search
    - **Task**: Add a robust implementation of the binary search algorithm, explaining the concept of monotonicity and providing a template for finding the first "true" value in a boolean-like sequence.
    - **Files**:
        - `content/fundamentals/binary_search.py`: Implement the binary search function and write a detailed docstring.
        - `stress-tests/fundamentals/binary_search.py`: Write a stress test that compares the custom implementation against Python's `bisect_left` module on a sorted array.
    - **Step Dependencies**: Step 49.
- [x] Step 52: Implement Two Pointers / Sliding Window
    - **Task**: Create a content file explaining and demonstrating the two-pointers and sliding window techniques with common patterns.
    - **Files**:
        - `content/fundamentals/two_pointers.py`: Implement an example problem's solution (e.g., longest substring with K distinct characters) and provide a thorough explanation in the docstring.
        - `stress-tests/fundamentals/two_pointers.py`: Write a stress test that validates the example problem's solution against a naive O(N^2) implementation.
    - **Step Dependencies**: Step 49.
- [x] Step 53: Implement Prefix Sums
    - **Task**: Implement 1D and 2D prefix sum arrays for fast range sum queries.
    - **Files**:
        - `content/fundamentals/prefix_sums.py`: Implement functions or classes for 1D and 2D prefix sums.
        - `stress-tests/fundamentals/prefix_sums.py`: Write a stress test that performs random range sum queries and validates the results against naively summing slices of the original array/grid.
    - **Step Dependencies**: Step 49.
- [x] Step 54: Implement Recursion and Backtracking Guide
    - **Task**: Create a content file that provides a template and explanation for recursion and backtracking, using "generating all subsets" as a primary example.
    - **Files**:
        - `content/fundamentals/recursion_backtracking.py`: Implement a backtracking function to generate all subsets. The docstring will explain the "choose-explore-unchoose" pattern.
        - `stress-tests/fundamentals/recursion_backtracking.py`: Write a test that compares the generated subsets against a known-correct iterative method (e.g., using bitmasks).
    - **Step Dependencies**: Step 49.
- [x] Step 55: Implement Greedy Algorithms Guide
    - **Task**: Add a content file explaining the greedy problem-solving paradigm.
    - **Files**:
        - `content/fundamentals/greedy_algorithms.py`: Use a classic problem (e.g., Activity Selection) to demonstrate the greedy approach. The docstring will focus on explaining the concept of a "greedy choice property" and "optimal substructure".
        - `stress-tests/fundamentals/greedy_algorithms.py`: Write a test that validates the greedy solution for the example problem against a correct, possibly slower, dynamic programming or brute-force solution.
    - **Step Dependencies**: Step 49.

## Phase 12: Standard Library Reference Implementation (New & Expanded)

This phase will add another new chapter, "Standard Library," to serve as a quick reference for Python modules that are exceptionally useful in competitive programming.

- [x] Step 56: Create "Standard Library" Chapter and `collections` Guide
    - **Task**: Create the directory structure for the "Standard Library" chapter. Add the first content file, focusing on the `collections` module.
    - **Files**:
        - `content/standard_library/`: Create the new directory.
        - `content/standard_library/chapter.tex`: Create the empty LaTeX chapter file.
        - `content/standard_library/collections_library.py`: Create the file with a docstring and examples for `deque`, `Counter`, and `defaultdict`.
        - `stress-tests/standard_library/`: Create the new directory.
        - `stress-tests/standard_library/collections_library.py`: Create a simple test script demonstrating the correct usage of each featured class.
    - **Step Dependencies**: Phase 11.
- [x] Step 57: Implement `heapq` Library Guide
    - **Task**: Add a content file explaining the use of the `heapq` module for min-priority queue operations on a standard Python list.
    - **Files**:
        - `content/standard_library/heapq_library.py`: Provide examples for `heappush`, `heappop`, and `heapify`.
        - `stress-tests/standard_library/heapq_library.py`: Write a test that pushes random elements and then pops them, asserting they are returned in sorted order.
    - **Step Dependencies**: Step 56.
- [x] Step 58: Implement `itertools` Library Guide
    - **Task**: Add a content file showcasing the most useful combinatorial functions from the `itertools` module.
    - **Files**:
        - `content/standard_library/itertools_library.py`: Provide examples for `permutations`, `combinations`, and `product`.
        - `stress-tests/standard_library/itertools_library.py`: Write a test comparing the output of these functions for small inputs against naive recursive implementations.
    - **Step Dependencies**: Step 56.
- [x] Step 59: Implement `bisect` Library Guide
    - **Task**: Add a content file explaining how to use the `bisect` module to efficiently search and maintain sorted lists.
    - **Files**:
        - `content/standard_library/bisect_library.py`: Provide examples for `bisect_left`, `bisect_right`, and `insort`.
        - `stress-tests/standard_library/bisect_library.py`: Write a test that verifies the insertion points returned by the `bisect` functions against a naive linear scan.
    - **Step Dependencies**: Step 56.
- [x] Step 60: Implement `functools` Library Guide
    - **Task**: Add a content file focusing on `@functools.cache` for providing easy memoization to recursive functions.
    - **Files**:
        - `content/standard_library/functools_library.py`: Use a recursive Fibonacci or a similar problem as a clear example of how `@cache` works.
        - `stress-tests/standard_library/functools_library.py`: Write a test to verify the correctness of the cached recursive solution against an iterative DP solution.
    - **Step Dependencies**: Step 56.
- [x] Step 61: Implement `math` Library Guide
    - **Task**: Add a content file highlighting useful functions from the `math` module.
    - **Files**:
        - `content/standard_library/math_library.py`: Provide examples for `gcd`, `ceil`, `floor`, `sqrt`, `isqrt`, `log2`, and `inf`.
        - `stress-tests/standard_library/math_library.py`: Write a test that verifies the output of these functions against expected values or other standard implementations (e.g., `math.gcd` vs. `fractions.gcd`).
    - **Step Dependencies**: Step 56.

## Phase 13: Final Integration (New)

- [x] Step 62: Integrate New Chapters into Main Document
    - **Task**: Update the main `pycpbook.tex` file to include the new "Fundamentals" and "Standard Library" chapters, ensuring they appear in the correct order in the final PDF and table of contents.
    - **Files**:
        - `content/pycpbook.tex`: Add `\chapter{Fundamentals}` and `\chapter{Standard Library}` with their corresponding `\input` commands.
    - **Step Dependencies**: Phase 12.

</implementation_plan>


Your task is to:

1. Identify the next incomplete step from the implementation plan (marked with `[ ]`)
2. Generate the necessary code for all files specified in that step
3. Return the generated code

The implementation plan is just a suggestion meant to provide a high-level overview of the objective. Use it to guide you, but you do not have to adhere to it strictly. Make sure to follow the given rules as you work along the lines of the plan.

For EVERY file you modify or create, you MUST provide the COMPLETE file contents in the format above.

Each file should be wrapped in a code block with its file path above it and a "Here's what I did and why":

Here's what I did and why: [text here...]
Filepath: src/components/Example.tsx

```
/**
 * @description
 * This component handles [specific functionality].
 * It is responsible for [specific responsibilities].
 *
 * Key features:
 * - Feature 1: Description
 * - Feature 2: Description
 *
 * @dependencies
 * - DependencyA: Used for X
 * - DependencyB: Used for Y
 *
 * @notes
 * - Important implementation detail 1
 * - Important implementation detail 2
 */

BEGIN WRITING FILE CODE
// Complete implementation with extensive inline comments & documentation...

```

Documentation requirements:

- File-level documentation explaining the purpose and scope
- Component/function-level documentation detailing inputs, outputs, and behavior
- Inline comments explaining complex logic or business rules
- Type documentation for all interfaces and types
- Notes about edge cases and error handling
- Any assumptions or limitations

Guidelines:

- Implement exactly one step at a time
- Ensure all code follows the project rules and technical specification
- Include ALL necessary imports and dependencies
- Write clean, well-documented code with appropriate error handling
- Always provide COMPLETE file contents - never use ellipsis (...) or placeholder comments
- Never skip any sections of any file - provide the entire file every time
- Handle edge cases and add input validation where appropriate
- Follow TypeScript best practices and ensure type safety
- Include necessary tests as specified in the testing strategy

Begin by identifying the next incomplete step from the plan, then generate the required code (with complete file contents and documentation).

Above each file, include a "Here's what I did and why" explanation of what you did for that file.

Then end with "STEP X COMPLETE. Here's what I did and why:" followed by an explanation of what you did and then a "USER INSTRUCTIONS: Please do the following:" followed by manual instructions for the user for things you can't do like installing libraries, updating configurations on services, etc.

You also have permission to update the implementation plan if needed. If you update the implementation plan, include ONLY the new modifications and return them as markdown code blocks at the end of the user instructions. NO NEED TO MARK TJE CIRRENT STEP AS COMPLETE - THAT IS IMPLIED. DO NOT OUTPUT THE IMPLEMENTATION PLAN IF YOU ARE NOT UPDATING IT.