def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("Simple Python Calculator")
    print("-------------------------")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers")
        return

    if choice == "1":
        result = add(num1, num2)
        operation = "+"
    elif choice == "2":
        result = subtract(num1, num2)
        operation = "-"
    elif choice == "3":
        result = multiply(num1, num2)
        operation = "*"
    else:
        result = divide(num1, num2)
        operation = "/"

    print(f"\nResult: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()
