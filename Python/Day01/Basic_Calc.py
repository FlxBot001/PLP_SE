# Basic Calculator Program

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        result = None  # Prevent undefined variable
    else:
        result = num1 / num2
else:
    print("Invalid operation. Please enter +, -, *, or /.")
    result = None  # Prevent undefined variable

# Print result if a valid operation was performed
if result is not None:
    print(f"Result: {num1} {operation} {num2} = {result}")
