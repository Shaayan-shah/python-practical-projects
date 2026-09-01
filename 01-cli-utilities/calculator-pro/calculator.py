"""
Arithmetic & Mathematical Calculator
Provides standard arithmetic operations, powers, modulo, square root,
and calculation history logging with clean error handling.
"""

import math
from typing import List, Tuple


class Calculator:
    """Performs arithmetic computations and tracks history."""

    def __init__(self):
        self.history: List[str] = []

    def add(self, a: float, b: float) -> float:
        res = a + b
        self._record(f"{a} + {b} = {res}")
        return res

    def subtract(self, a: float, b: float) -> float:
        res = a - b
        self._record(f"{a} - {b} = {res}")
        return res

    def multiply(self, a: float, b: float) -> float:
        res = a * b
        self._record(f"{a} * {b} = {res}")
        return res

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero is undefined.")
        res = a / b
        self._record(f"{a} / {b} = {res}")
        return res

    def power(self, base: float, exponent: float) -> float:
        res = base ** exponent
        self._record(f"{base} ^ {exponent} = {res}")
        return res

    def modulus(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Modulus with zero divisor is undefined.")
        res = a % b
        self._record(f"{a} % {b} = {res}")
        return res

    def square_root(self, a: float) -> float:
        if a < 0:
            raise ValueError("Square root of a negative number is undefined for real numbers.")
        res = math.sqrt(a)
        self._record(f"sqrt({a}) = {res}")
        return res

    def _record(self, entry: str):
        self.history.append(entry)

    def print_history(self):
        if not self.history:
            print("\n[History] No calculations recorded yet.")
            return
        print("\n--- Calculation History ---")
        for i, item in enumerate(self.history, start=1):
            print(f"  {i}. {item}")
        print("---------------------------")


def get_two_numbers() -> Tuple[float, float]:
    num1 = float(input("Enter first number: ").strip())
    num2 = float(input("Enter second number: ").strip())
    return num1, num2


def main():
    calc = Calculator()
    print("==================================================")
    print("           ARITHMETIC & MATH CALCULATOR           ")
    print("==================================================")

    while True:
        print("\nOperations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Modulus (%)")
        print("7. Square Root (sqrt)")
        print("8. View History")
        print("9. Exit")

        choice = input("\nSelect operation (1-9): ").strip()

        try:
            if choice == "1":
                a, b = get_two_numbers()
                print(f"\nResult: {a} + {b} = {calc.add(a, b)}")
            elif choice == "2":
                a, b = get_two_numbers()
                print(f"\nResult: {a} - {b} = {calc.subtract(a, b)}")
            elif choice == "3":
                a, b = get_two_numbers()
                print(f"\nResult: {a} * {b} = {calc.multiply(a, b)}")
            elif choice == "4":
                a, b = get_two_numbers()
                print(f"\nResult: {a} / {b} = {calc.divide(a, b)}")
            elif choice == "5":
                a, b = get_two_numbers()
                print(f"\nResult: {a} ^ {b} = {calc.power(a, b)}")
            elif choice == "6":
                a, b = get_two_numbers()
                print(f"\nResult: {a} % {b} = {calc.modulus(a, b)}")
            elif choice == "7":
                num = float(input("Enter number: ").strip())
                print(f"\nResult: sqrt({num}) = {calc.square_root(num)}")
            elif choice == "8":
                calc.print_history()
            elif choice == "9":
                print("\nCalculator closed. Have a great day!")
                break
            else:
                print("[Error] Invalid selection. Choose a number between 1 and 9.")
        except ValueError as e:
            print(f"[Input Error] {e}")
        except ZeroDivisionError as e:
            print(f"[Math Error] {e}")


if __name__ == "__main__":
    main()
