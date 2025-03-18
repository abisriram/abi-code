def calculator(choice, num1, num2):
    match choice:
        case 1:
            return num1 + num2
        case 2:
            return num1 - num2
        case 3:
            return num1 * num2
        case 4:
            return num1 / num2 if num2 != 0 else "Cannot divide by zero"
        case _:
            return "Invalid choice"

# User input
print("Select operation:")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = int(input("Enter choice (1/2/3/4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = calculator(choice, num1, num2)
print("Result:", result)
