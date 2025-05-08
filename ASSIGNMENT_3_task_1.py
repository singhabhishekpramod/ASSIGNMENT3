#Task 1: Calculate Factorial Using a Function
def calculate_factorial(n):
    try:
        if n < 0:
            return "Factorial is not defined for negative numbers."
        elif n % 1 != 0:
            return "Factorial is only defined for integers."
        else:
            result = 1
            for i in range(1, int(n) + 1):
                result *= i
            return result
    except OverflowError:
        return "Factorial result is too large."

def main():
    try:
        num = float(input("Enter a number: "))
        result = calculate_factorial(num)
        print(f"The factorial of {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()