import sys
import os

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

# Ensure correct number of arguments
if len(sys.argv) != 4:
    print("Usage: python script.py <num1> <operation> <num2>")
    sys.exit(1)

# Parse command-line arguments
num1 = float(sys.argv[1])
operation = sys.argv[2].lower()  # Convert to lowercase for consistency
num2 = float(sys.argv[3])

# Perform the operation
if operation in ("add", "+", "plus"):
    output = add(num1, num2)
elif operation in ("sub", "-", "minus"):
    output = sub(num1, num2)
elif operation in ("mul", "*", "multiply"):
    output = mul(num1, num2)
else:
    print("Invalid operation. Use add (+), sub (-), or mul (*).")
    sys.exit(1)

print(output)

print(os.getenv("password"))  #example for env variablesls

