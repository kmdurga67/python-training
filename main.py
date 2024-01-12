
import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <operator> <number2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        operator = sys.argv[2]
        num2 = float(sys.argv[3])

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator. Please use +, -, *, /")
            sys.exit(1)

        print(f"Result: = {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        sys.exit(1)

if __name__ == "__main__":
    main()
