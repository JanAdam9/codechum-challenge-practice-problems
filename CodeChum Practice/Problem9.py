# Create a calculator that performs basic operations (+, -, *, /, %). The program should validate that division/modulo by zero is not allowed.

num1 = int(input())
num2 = int(input())
operation = input()
result = 0

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero")
        quit()
    else:
        result = num1 / num2
elif operation == "%":
    if num2 == 0:
        print("Error: Division by zero")
        quit()
    else:
        result = num1 % num2
else:
    print("Unknown operation")

print(f"Result: {result:.2f}")