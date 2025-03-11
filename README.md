# Python Arithmetic CLI

## Overview
This project provides a simple command-line interface (CLI) to perform basic arithmetic operations.

## Folder Structure
```
PLP-learning/
│── main.py                    # Entry point for the CLI
│── week_3/
│   │── __init__.py            # Marks the folder as a package
│   │── python_arithmetics_day_1.py  # Contains arithmetic_math_calculator function
│── README.md                  # Documentation
```

## Installation
1. Clone the repository:
   ```sh
   git clone <repo-link>
   cd PLP-learning
   ```
2. Set up a virtual environment (optional but recommended):
   ```sh
   python -m venv env
   source env/bin/activate  # On macOS/Linux
   env\Scripts\activate     # On Windows
   ```
3. Ensure Python is installed (Python 3.x required).

## Usage
Run the following command in your terminal:

```sh
py main.py run arithmetics
```
This will start the arithmetic calculator where you can input two numbers and an operator (+, -, *, /).

### Help Command
To get a list of available commands:
```sh
py main.py --help
```

### Info Command
To display file details:
```sh
py main.py --info
```

## Features
- Performs addition, subtraction, multiplication, and division.
- Provides error handling for invalid inputs.
- Displays usage instructions via `--help`.

## Example Execution
```
$ py main.py run arithmetics
Enter First Number: 10
Enter an operation (+, -, *, /): +
Enter Second Number: 5
10 + 5 = 15
```

## Troubleshooting
- Ensure you are running the script from the project root directory.
- If you get `ModuleNotFoundError`, make sure `week_3/__init__.py` exists.
- If using a virtual environment, activate it before running the script.