from choices import select_operator
from operations import add, subtract, multiply, divide

def main():
    while True:
        choice = select_operator()

        if choice.lower() == 'exit':
            print("Completed the program. Goodbye!")
            break

        if choice in ['Add', 'Sub', 'Multiply', 'Divide']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 'Add':
                result = add(num1, num2)

            elif choice == 'Sub':
                result = subtract(num1, num2)

            elif choice == 'Multiply':
                result = multiply(num1, num2)

            elif choice == 'Divide':
                result = divide(num1, num2)

            print(f"Your Result = {result}")

        else:
            print("Invalid Input. Please enter a valid choice (Add/ Sub/ Multiply/ Divide) or type 'exit' to end the program.")

if __name__ == "__main__":
    main()
