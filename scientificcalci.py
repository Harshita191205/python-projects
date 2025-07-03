import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    return x / y

def power(x, y):
    return x ** y

def root(x, y):
    if x < 0 and y % 2 == 0:
        return "Error: Negative number cannot have even root"
    return x ** (1/y)

def log(x, base):
    if x <= 0:
        return "Error: Logarithm of non-positive number is not defined"
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def main():
    print("Scientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Quit")

    while True:
        choice = int(input("Enter your choice (1-11): "))
        if choice == 11:
            break

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print("Result: ", add(num1, num2))
            elif choice == 2:
                print("Result: ", subtract(num1, num2))
            elif choice == 3:
                print("Result: ", multiply(num1, num2))
            elif choice == 4:
                print("Result: ", divide(num1, num2))

        elif choice == 5:
            num1 = float(input("Enter base number: "))
            num2 = float(input("Enter exponent: "))
            print("Result: ", power(num1, num2))

        elif choice == 6:
            num1 = float(input("Enter number: "))
            num2 = float(input("Enter root: "))
            print("Result: ", root(num1, num2))

        elif choice == 7:
            num1 = float(input("Enter number: "))
            base = float(input("Enter base: "))
            print("Result: ", log(num1, base))

        elif choice in [8, 9, 10]:
            num1 = float(input("Enter angle in degrees: "))

            if choice == 8:
                print("Result: ", sin(num1))
            elif choice == 9:
                print("Result: ", cos(num1))
            elif choice == 10:
                print("Result: ", tan(num1))

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()