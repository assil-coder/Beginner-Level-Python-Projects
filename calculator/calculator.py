try:
    num1 = int(input("Enter your first number:\n"))
    num2 = int(input("Enter your second number:\n"))
    operation = input("Enter your operation (+) (-) (/) (*):\n")
    
    if operation == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    elif operation == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    else:
        print("Invalid operation! Please use +, -, *, or /")
        
except ValueError:
    print("Error: Please enter valid numbers!")