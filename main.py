import sys
from week_3.python_arithmetics_day_1 import arithmetic_math_calculator

def main():
    '''
    main method that handles command line commands
    '''
    # arithmetics command
    if len(sys.argv) == 3 and sys.argv[1] == 'run' and sys.argv[2] == 'arithmetics':
        print(" Intro to Python Assignment: Week 3 Day 1 Assignment -> file is python_basics_week_3_day_1.py ")
        arithmetic_math_calculator()
    # help command
    elif len(sys.argv) == 2 and sys.argv[1] == '--help':
        print("Usage: py main.py run <key_word>")
        print("Available key words:")
        print("  arithmetics - Runs the arithmetic calculator")
        print("  --help      - Displays this help message")
    elif len(sys.argv) == 2 and sys.argv[1] == '--info':
        # files
        print(" Main where all executions are -> file is main.py ")
        print(" Intro to Python Assignment: Week 3 Day 1 Assignment -> file is python_basics_week_3_day_1.py ")
        # commands
        print("For mor commands: ")
        print("For more help, type: py main.py --help")
    else:
        print("Invalid command.")
        print("Usage: py main.py run <key_word>")
        print("For more help, type: py main.py --help")

if __name__ == "__main__":
    main()