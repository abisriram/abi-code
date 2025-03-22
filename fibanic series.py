def fibonacci_recursive(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

n = int(input("Enter n: "))
print(f"The {n}th Fibonacci number is: {fibonacci_recursive(n)}")