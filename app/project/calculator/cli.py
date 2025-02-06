# calculator/cli.py
import argparse
from .core import add_numbers

def main():
    parser = argparse.ArgumentParser(description="Simple calculator to add two numbers.")
    parser.add_argument('num1', type=float, help="First number")
    parser.add_argument('num2', type=float, help="Second number")
    args = parser.parse_args()

    try:
        result = add_numbers(args.num1, args.num2)
        print(f"The sum of {args.num1} and {args.num2} is {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()