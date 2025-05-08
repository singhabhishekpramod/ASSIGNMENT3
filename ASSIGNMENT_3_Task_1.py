#Task 1: Calculate Factorial Using a Function
import math

def get_user_input():
    while True:
        try:
            num = float(input("Enter a number: "))
            if num < 0:
                print("Please enter a non-negative number for square root and factorial calculation.")
                continue
            if num <= 0:
                print("Please enter a positive number for natural logarithm calculation.")
                continue
            if num % 1 != 0:
                print("Please enter an integer for factorial calculation.")
                continue
            return int(num)
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_results(num):
    square_root = math.sqrt(num)
    natural_logarithm = math.log(num)
    sine = math.sin(num)
    factorial = math.factorial(num)
    return square_root, natural_logarithm, sine, factorial

def main():
    num = get_user_input()
    square_root, natural_logarithm, sine, factorial = calculate_results(num)
    print(f"Results for {num}:")
    print(f"Square root: {square_root}")
    print(f"Natural logarithm: {natural_logarithm}")
    print(f"Sine (in radians): {sine}")
    print(f"Factorial: {factorial}")

if __name__ == "__main__":
    main()
