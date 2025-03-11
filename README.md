# Python Arithmetic, DSA & Functions CLI

## Overview
This project provides a command-line interface (CLI) to perform basic arithmetic operations, data structure manipulations, and function-based discount calculations.

## Folder Structure
```
PLP-learning/
│── main.py                    # Entry point for the CLI
│── week_3/
│   │── __init__.py             # Marks the folder as a package
│   │── python_arithmetics_day_1.py  # Contains arithmetic_math_calculator function
│   │── python_dsa_day_2.py     # Contains data_structures function
│   │── python_function_flow_day_3.py  # Contains discount_prompter function
│── README.md                   # Documentation
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
Run the following commands in your terminal:

### Arithmetic Calculator
```sh
py main.py run arithmetics
```
This will start the arithmetic calculator where you can input two numbers and an operator (+, -, *, /).

### Data Structures Operations
```sh
py main.py run dsa
```
This will execute a sequence of list operations, including appending, inserting, extending, sorting, and finding an index.

### Function-based Discount Calculation
```sh
py main.py run functions
```
This will prompt the user to enter an original price and discount percentage, then determine if a discount is applied based on the given criteria.

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
- Performs arithmetic calculations (addition, subtraction, multiplication, and division).
- Provides data structure operations on lists.
- Applies discounts based on specified conditions.
- Handles invalid inputs with error messages.
- Displays usage instructions via `--help`.

## Example Execution
### Arithmetic Calculator
```
$ py main.py run arithmetics
Enter First Number: 10
Enter an operation (+, -, *, /): +
Enter Second Number: 5
10 + 5 = 15
```

### Data Structures
```
$ py main.py run dsa
My list currently: [10, 20, 30, 40]
My list after inserting 15 after 10 or at index 1: [10, 15, 20, 30, 40]
My list after extending with list [50, 60, 70]: [10, 15, 20, 30, 40, 50, 60, 70]
My list after removing last item on the list: [10, 15, 20, 30, 40, 50, 60]
My list after sorting list in ascending order: [10, 15, 20, 30, 40, 50, 60]
Index of 30 in my_list: 3
```

### Discount Calculation
```
$ py main.py run functions
Enter Original price of item: 100
Enter discount on the item in Percentage(%): 25
Final price of 100 and discount percentage 25% is 75.00
Price remains: 75.00
```

```
$ py main.py run functions
Enter Original price of item: 100
Enter discount on the item in Percentage(%): 15
Discount is less than 20%
Price remains: 100.00
```

## Troubleshooting
- Ensure you are running the script from the project root directory.
- If you get `ModuleNotFoundError`, make sure `week_3/__init__.py` exists.
- If using a virtual environment, activate it before running the script.

## Contribution
Feel free to contribute by submitting pull requests or reporting issues.

## License
MIT License

