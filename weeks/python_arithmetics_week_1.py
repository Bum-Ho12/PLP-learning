'''
python file to handle basic python arithmetics
'''

# method to perform arithmetics
def arithmetic_math_calculator():
    try:
        a = float(input("Enter First Number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        b = float(input("Enter Second Number: "))

        if operator == '+':
            ans = a + b
        elif operator == '-':
            ans = a-b
        elif operator == '/':
            if b == 0:
                print("Division by  zero is not allowed.")
                return
            ans = a/b
        elif operator == '*':
            ans = a * b
            return
        else:
            print("No such operand is recognized, please enter either of these + , - , * , / ")

        print(f"{a} {operator} {b} = {ans}")

    except valueError:
        print(" ****** Invalid. Enter valid arithmetic values. ******")