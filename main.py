import sys
from weeks.python_arithmetics_week_1 import arithmetic_math_calculator
from weeks.python_dsa_week_2 import data_structures
from weeks.python_function_flow_week_3 import discount_prompter
from weeks.python_file_handling_week_4 import file_prompter

def main():
    '''
    main method that handles command line commands
    '''
    # arithmetics command
    if len(sys.argv) == 3 and sys.argv[1] == 'run' and sys.argv[2] == 'arithmetics':
        print(" Intro to Python Assignment: Week 1 Assignment -> file is python_arithmetics_week_1.py ")
        arithmetic_math_calculator()

    # DSA command
    elif len(sys.argv) == 3 and sys.argv[1] == 'run' and sys.argv[2] == 'dsa':
        print(" Intro to Python Assignment: Week 2 Assignment -> file is python_dsa_week_2.py ")
        data_structures()

    # control flow and functions command
    elif len(sys.argv) == 3 and sys.argv[1] == 'run' and sys.argv[2] == 'functions':
        print(" Intro to Python Assignment: Week 3 Assignment -> file is python_function_flow_week_3.py ")
        discount_prompter()

    # file handling command
    elif len(sys.argv) == 3 and sys.argv[1] == 'run' and sys.argv[2] == 'files':
        print(" Intro to Python Assignment: Week 4 Assignment -> file is python_file_handling_week_4.py ")
        file_prompter()

    # help command
    elif len(sys.argv) == 2 and sys.argv[1] == '--help':
        print("Usage: py main.py run <key_word>")
        print("Available key words:")
        print("  arithmetics - Runs the arithmetic calculator")
        print("  --help      - Displays this help message")

    # --info command
    elif len(sys.argv) == 2 and sys.argv[1] == '--info':
        # files
        print(" Main where all executions are -> file is main.py ")
        print(" Intro to Python Assignment: Week 1 Assignment -> file is python_arithmetics_week_1.py ")
        print(" Intro to Python Assignment: Week 2 Assignment -> file is python_dsa_week_2.py ")
        print(" Intro to Python Assignment: Week 3 Assignment -> file is python_function_flow_week_3.py ")
        print(" Intro to Python Assignment: Week 4 Assignment -> file is python_file_handling_week_4.py ")
        # commands
        print("For mor commands: ")
        print("For more help, type: py main.py --help")

    # if errors
    else:
        print("Invalid command.")
        print("Usage: py main.py run <key_word>")
        print("For more help, type: py main.py --help")
        print("For Information, type: py main.py --info")

if __name__ == "__main__":
    main()