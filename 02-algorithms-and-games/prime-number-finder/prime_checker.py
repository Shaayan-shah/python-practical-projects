"""
Primality Verification & Sieve of Eratosthenes Engine
Mathematical algorithms for checking individual prime numbers in O(sqrt(N)) time
and generating prime sequences across large numeric ranges.
"""

import time
from typing import List


def is_prime(number: int) -> bool:
    """
    Check if a single integer is prime using O(sqrt(N)) trial division with 6k +/- 1 step.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """
    Generate all prime numbers up to `limit` using the Sieve of Eratosthenes algorithm.
    Time Complexity: O(N log log N)
    """
    if limit < 2:
        return []

    is_prime_flags = [True] * (limit + 1)
    is_prime_flags[0] = is_prime_flags[1] = False

    for factor in range(2, int(limit ** 0.5) + 1):
        if is_prime_flags[factor]:
            for multiple in range(factor * factor, limit + 1, factor):
                is_prime_flags[multiple] = False

    return [num for num, prime in enumerate(is_prime_flags) if prime]


def main():
    print("==================================================")
    print("       PRIMALITY TESTER & SIEVE GENERATOR         ")
    print("==================================================")

    try:
        test_val = int(input("Enter an integer to test for primality: ").strip())
        if is_prime(test_val):
            print(f"[Result] {test_val} is a PRIME number!")
        else:
            print(f"[Result] {test_val} is a COMPOSITE number.")
    except ValueError:
        print("[Error] Please enter a valid integer.")

    print("\n--- Prime Range Generator ---")
    try:
        limit_val = int(input("Generate all prime numbers up to (e.g. 100): ").strip())
        start_time = time.perf_counter()
        primes = sieve_of_eratosthenes(limit_val)
        elapsed_ms = (time.perf_counter() - start_time) * 1000.0

        print(f"\nFound {len(primes)} primes up to {limit_val} in {elapsed_ms:.3f} ms:")
        print(primes[:30], "..." if len(primes) > 30 else "")
    except ValueError:
        print("[Error] Invalid integer limit.")


if __name__ == "__main__":
    main()
