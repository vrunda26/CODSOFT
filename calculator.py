def calculator():
    print("**********Simple Calculator**********")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    choice = input("Choose operation (1/2/3/4): ")
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        result = num1 / num2
        operation = '/'
    else:
        print("Invalid numbers!")
        return
    print(f"\nResult: {num1} {operation} {num2} = {result}")
calculator()
