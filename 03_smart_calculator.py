"""Create a calculator that takes two numbers and an operation (+, -, *, /, %, **) from user input.
Include error handling for division by zero and invalid operations."""
try:
    num1 = float(input("enter the number: "))
    operator = (input("enter the operation: "))
    num2 = float(input("enter the number: "))



    if operator == "+":
        print(num1 + num2)

    elif operator == "-":
        print(num1 - num2)

    elif operator == "*":
        print(num1 * num2)

    elif operator == "%":
        try:
            print(num1 % num2)
        except ZeroDivisionError:
            print("cannot be divisible by 0")
    elif operator == "**":
        print(num1 ** num2)

    elif operator == "/":
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("cannot be divisible by 0")
            
    else:
        print("Enter the correct operator")

except ValueError:
    print("Make sure your values are correct")