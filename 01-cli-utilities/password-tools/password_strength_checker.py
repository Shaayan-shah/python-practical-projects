"""
Password Strength & Entropy Analyzer
Evaluates password complexity, Shannon entropy, and character diversity.
"""

import math
import string
from typing import Dict, Any


def calculate_entropy(password: str) -> float:
    """Calculate Shannon entropy bits."""
    pool_size = 0
    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += 32

    if pool_size == 0 or len(password) == 0:
        return 0.0

    return len(password) * math.log2(pool_size)


def evaluate_password(password: str) -> Dict[str, Any]:
    """Analyze password complexity."""
    entropy = calculate_entropy(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)
    is_length_ok = len(password) >= 12

    score = sum([is_length_ok, has_lower and has_upper, has_digit, has_symbol, entropy >= 60.0])

    ratings = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    return {
        "rating": ratings.get(score, "Fair"),
        "score": score,
        "entropy_bits": round(entropy, 1),
        "length": len(password),
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digits": has_digit,
        "has_symbols": has_symbol
    }


def main():
    print("==================================================")
    print("          PASSWORD STRENGTH ANALYZER              ")
    print("==================================================")

    test_pw = input("Enter password to analyze: ").strip()
    if not test_pw:
        test_pw = "P@ssw0rd2026!"

    res = evaluate_password(test_pw)

    print(f"\nPassword Length: {res['length']} characters")
    print(f"Strength Rating: {res['rating']} (Score: {res['score']}/5)")
    print(f"Shannon Entropy: {res['entropy_bits']} bits")
    print("\nCriteria Checklist:")
    print(f"  [{'✓' if res['has_upper'] else '✗'}] Uppercase letters (A-Z)")
    print(f"  [{'✓' if res['has_lower'] else '✗'}] Lowercase letters (a-z)")
    print(f"  [{'✓' if res['has_digits'] else '✗'}] Numerical digits (0-9)")
    print(f"  [{'✓' if res['has_symbols'] else '✗'}] Special symbols (!@#$)")
    print(f"  [{'✓' if res['length'] >= 12 else '✗'}] Length >= 12 chars")


if __name__ == "__main__":
    main()
