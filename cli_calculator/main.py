from calculator.operations import add, subtract, multiply, divide


def perform_operation(num1, operator, num2):
    if operator == 'add':
        return add(num1, num2)
    elif operator == 'sub':
        return subtract(num1, num2)
    elif operator == 'mult':
        return multiply(num1, num2)
    elif operator == 'div':
        return divide(num1, num2)
    else:
        return "Invalid operator. Please use add, sub, mult, div"


def main():
    while True:
        input_str = input(
            "Enter values like <number1> <operator> <number2> (or type 'exit' to end the program): ")

        if input_str.lower() == 'exit':
            break

        values = input_str.split()
        if len(values) != 3:
            print(
                "Invalid input. Please enter values like <number1> <operator> <number2>.")
            continue

        num1 = float(values[0])
        operator = values[1]
        num2 = float(values[2])
        result = perform_operation(num1, operator, num2)
        print(result)


if __name__ == "__main__":
    main()
