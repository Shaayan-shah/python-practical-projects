"""
Bidirectional Palindrome Symmetry Engine
Validates strings, phrases, and numeric inputs for palindromic symmetry,
ignoring case, spaces, and non-alphanumeric punctuation.
"""

import re


def is_palindrome(input_val: str) -> bool:
    """
    Returns True if the normalized input reads the exact same forwards and backwards.
    Normalizes by stripping non-alphanumeric characters and converting to lowercase.
    """
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", str(input_val)).lower()
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]


def main():
    print("==================================================")
    print("          PALINDROME SYMMETRY VALIDATOR           ")
    print("==================================================")

    sample = input("Enter a word, sentence, or number to check: ").strip()
    if not sample:
        sample = "A man, a plan, a canal: Panama"

    result = is_palindrome(sample)
    print(f"\nInput   : \"{sample}\"")
    print(f"Result  : {'[PASS] PALINDROME' if result else '[FAIL] NOT A PALINDROME'}\n")

    print("--- Benchmark Test Cases ---")
    test_cases = [
        "madam",
        "racecar",
        "Was it a car or a cat I saw?",
        "1234321",
        "Hello Python"
    ]
    for text in test_cases:
        status = "[YES]" if is_palindrome(text) else "[NO ]"
        print(f"  {status} {text}")


if __name__ == "__main__":
    main()
