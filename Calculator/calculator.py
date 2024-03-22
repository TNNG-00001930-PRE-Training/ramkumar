def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    while True:
        try:
            print("Operations:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")
            select = int(input("Enter operation number: "))
            
            if select == 5:
                print("Exiting calculator.")
                break

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if select == 1:
                print("Result:", add(num1, num2))
            elif select == 2:
                print("Result:", subtract(num1, num2))
            elif select == 3:
                print("Result:", multiply(num1, num2))
            elif select == 4:
                print("Result:", divide(num1, num2))
            else:
                print("Invalid choice. Please enter a valid operation number.")
        except ValueError as e:
            print("Error:", e)
            print("Please enter numeric values.")


calculator()
