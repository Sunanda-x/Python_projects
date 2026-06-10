while True:
    print("\n--- Calculator ---")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        print("Result =", num1 + num2)

    elif operation == "-":
        print("Result =", num1 - num2)

    elif operation == "*":
        print("Result =", num1 * num2)

    elif operation == "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero.")

    else:
        print("Invalid operation.")

    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() != "yes":
        print("Thank you for using Calculator!")
        break