"""
Cryptographically Secure Password Generator
Generates high-entropy random passwords using Python's `secrets` module.
"""

import string
import secrets
from typing import List


def generate_secure_password(length: int = 16, use_symbols: bool = True, use_numbers: bool = True) -> str:
    """Generate a cryptographically secure random password."""
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits if use_numbers else ""
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?" if use_symbols else ""

    password_chars: List[str] = [
        secrets.choice(lower),
        secrets.choice(upper)
    ]
    if use_numbers:
        password_chars.append(secrets.choice(digits))
    if use_symbols:
        password_chars.append(secrets.choice(symbols))

    all_chars = lower + upper + digits + symbols
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(all_chars))

    for i in range(len(password_chars) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password_chars[i], password_chars[j] = password_chars[j], password_chars[i]

    return "".join(password_chars)


def main():
    print("==================================================")
    print("       CRYPTOGRAPHIC PASSWORD GENERATOR           ")
    print("==================================================")

    try:
        length_input = input("Enter desired password length (min 8) [16]: ").strip() or "16"
        length = int(length_input)
        symbols = input("Include special symbols (!@#$)? (y/n) [y]: ").strip().lower() != "n"
        numbers = input("Include numbers (0-9)? (y/n) [y]: ").strip().lower() != "n"

        print("\nGenerated Secure Passwords:")
        for i in range(3):
            pw = generate_secure_password(length, use_symbols=symbols, use_numbers=numbers)
            print(f"  Option {i+1}: {pw}")
    except ValueError as e:
        print(f"[Error] {e}")


if __name__ == "__main__":
    main()
