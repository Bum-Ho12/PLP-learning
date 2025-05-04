# Python Arithmetic & DSA CLI

## Overview
This project provides a command-line interface (CLI) to perform basic arithmetic operations, data structure manipulations, and control flow functions.

## Folder Structure
```
PLP-learning/
│── main.py                    # Entry point for the CLI
│── weeks/
│   │── __init__.py            # Marks the folder as a package
│   │── python_arithmetics_week_1.py  # Contains arithmetic_math_calculator function
│   │── python_dsa_week_2.py  # Contains data_structures function
│   │── python_function_flow_week_3.py  # Contains discount_prompter function
│   │── python_file_handling_week_4.py  # Contains file_prompter function
│   │── python_oop_week_5.py  # Contains class_prompter and vehicle_prompter function
│   │── python_iris_week_7.ipynb
│   │── python_data_analysis_week_8.ipynb
│── README.md                  # Documentation
│── requirements.txt                 # packages
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
4. Install packages:
   ```sh
   pip install -r requirements.txt
   ```

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

### Control Flow and Functions
```sh
py main.py run functions
```
This will execute a function that calculates discounts based on user input.

### File Handling
```sh
py main.py run files
```
This will execute a function that reads and modifies a file added as a input.

### OOP
```sh
py main.py run oop assignment_1
py main.py run oop assignment_2
```
These 2 commands will execute the 2 assignments for week 5 OOP.

### Iris Dataset
```sh
py main.py run iris
```
This will execute the iris ipynb file and invoke the code on browser(default).

### Data Analysis Dataset
```sh
py main.py run data_analysis
```
This will execute the data analysis ipynb file and invoke the code on browser(default).

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
- Implements a function to calculate discounts based on user input.
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

### Discount Function
```
$ py main.py run functions
Enter Original price of item: 1000
Enter discount on the item in Percentage(%): 25
Final price of 1000 and discount percentage 25% is 750.00
```

## Troubleshooting
- Ensure you are running the script from the project root directory.
- If you get `ModuleNotFoundError`, make sure `weeks/__init__.py` exists.
- If using a virtual environment, activate it before running the script.

## Contribution
Feel free to contribute by submitting pull requests or reporting issues.

## License
MIT License

