import sys
import nbformat
import asyncio
import subprocess
import os
from nbconvert.preprocessors import ExecutePreprocessor
from weeks.python_arithmetics_week_1 import arithmetic_math_calculator
from weeks.python_dsa_week_2 import data_structures
from weeks.python_function_flow_week_3 import discount_prompter
from weeks.python_file_handling_week_4 import file_prompter
from weeks.python_oop_week_5 import super_hero_prompter, vehicle_prompter

def run_notebook(path):
    with open(path) as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'path': './weeks'}})

def open_notebook_in_browser(path):
    """Launch the Jupyter notebook interface with the specified notebook."""
    notebook_dir = os.path.dirname(os.path.abspath(path))
    notebook_name = os.path.basename(path)

    print(f"Launching Jupyter notebook interface for {notebook_name}...")
    subprocess.Popen(['jupyter', 'notebook', notebook_name],
                    cwd=notebook_dir)

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

    # oop commands
    elif len(sys.argv) == 4 and sys.argv[1] == 'run' and sys.argv[2] == 'oop':
        print(" Intro to Python Assignment: Week 5 Assignment -> file is python_oop_week_5.py ")
        if sys.argv[3] == 'assignment_1':
            super_hero_prompter()
        elif sys.argv[3] == 'assignment_2':
            vehicle_prompter()
        else:
            print("Invalid command.")
            print("Usage: py main.py run oop <sub_command>")
            print("Available sub_commands: assignment_1, assignment_2")

    # iris notebook command
    elif len(sys.argv) == 3 and sys.argv[1] == 'run' and sys.argv[2] == 'iris':
        print(" Intro to Python Assignment: Week 7 Assignment -> file is python_iris_week_7.ipynb ")
        notebook_path = './weeks/python_iris_week_7.ipynb'

        if len(sys.argv) > 3 and sys.argv[3] == '--execute':
            # Only execute the notebook without opening the interface
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            run_notebook(notebook_path)
        else:
            # Open the notebook in the Jupyter interface
            open_notebook_in_browser(notebook_path)

    # help command
    elif len(sys.argv) == 2 and sys.argv[1] == '--help':
        print("Usage: py main.py run <key_word> [options]")
        print("Available key words:")
        print("  arithmetics - Runs the arithmetic calculator")
        print("  dsa - Runs the data structures assignment")
        print("  functions - Runs the control flow and functions assignment")
        print("  files - Runs the file handling assignment")
        print("  oop - Runs the oop assignment")
        print("  iris - Opens the iris data jupyter notebook in browser")
        print("         Use with --execute to run without opening browser")
        print("  --help      - Displays this help message")

    # --info command
    elif len(sys.argv) == 2 and sys.argv[1] == '--info':
        # files
        print(" Main where all executions are -> file is main.py ")
        print(" Intro to Python Assignment: Week 1 Assignment -> file is python_arithmetics_week_1.py ")
        print(" Intro to Python Assignment: Week 2 Assignment -> file is python_dsa_week_2.py ")
        print(" Intro to Python Assignment: Week 3 Assignment -> file is python_function_flow_week_3.py ")
        print(" Intro to Python Assignment: Week 4 Assignment -> file is python_file_handling_week_4.py ")
        print(" Intro to Python Assignment: Week 5 Assignment -> file is python_oop_week_5.py ")
        print(" Intro to Python Assignment: Week 7 Assignment -> file is python_iris_week_7.ipynb ")
        # commands
        print("For more commands: ")
        print("For more help, type: py main.py --help")

    # if errors
    else:
        print("Invalid command.")
        print("Usage: py main.py run <key_word>")
        print("For more help, type: py main.py --help")
        print("For Information, type: py main.py --info")

if __name__ == "__main__":
    main()