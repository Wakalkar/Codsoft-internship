def add(a, b):
    """Function to add two numbers."""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers."""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b

def divide(a, b):
    """Function to divide two numbers."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def calculator(num1, num2, choice):
    """Function to perform basic arithmetic operations based on user input."""
    if choice == '1':
        return f"Result: {num1} + {num2} = {add(num1, num2)}"
    elif choice == '2':
        return f"Result: {num1} - {num2} = {subtract(num1, num2)}"
    elif choice == '3':
        return f"Result: {num1} * {num2} = {multiply(num1, num2)}"
    elif choice == '4':
        return f"Result: {num1} / {num2} = {divide(num1, num2)}"
    else:
        return "Error: Invalid operation choice."

if __name__ == "__main__":
    print("\nWelcome to the Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        # Prompt the user to input numbers manually
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Prompt the user to select an operation
        print("\nSelect the operation:")
        print("1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division")
        choice = input("Enter your choice (1/2/3/4): ")

        # Perform the operation and display the result
        print(calculator(num1, num2, choice))
    except ValueError:
        print("Error: Please enter valid numeric values.")

