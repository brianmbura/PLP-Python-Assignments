# Simple calculator program

# Ask the user to input the first number
num1 = float(input("Enter the 1st number: "))

# Ask the user to input the second number
num2 = float(input("Enter the 2nd number: "))

# Ask the user to input the operation
operation = input("Operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
