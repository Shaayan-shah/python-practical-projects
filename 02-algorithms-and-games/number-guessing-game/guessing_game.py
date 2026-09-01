"""
Interactive Binary-Search Number Guessing Game
Randomized numerical game featuring difficulty modes, binary search feedback (Higher/Lower),
and attempt performance metrics.
"""

import random


def play_game():
    print("==================================================")
    print("             NUMBER GUESSING GAME                 ")
    print("==================================================")

    print("\nSelect Difficulty:")
    print("1. Easy   (Range 1 to 50,  10 attempts)")
    print("2. Medium (Range 1 to 100,  7 attempts)")
    print("3. Hard   (Range 1 to 500,  9 attempts)")

    choice = input("\nChoose difficulty (1-3) [2]: ").strip() or "2"
    if choice == "1":
        max_num, max_attempts = 50, 10
    elif choice == "3":
        max_num, max_attempts = 500, 9
    else:
        max_num, max_attempts = 100, 7

    secret_number = random.randint(1, max_num)
    print(f"\nI have selected a secret number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    attempts_used = 0
    while attempts_used < max_attempts:
        attempts_used += 1
        remaining = max_attempts - attempts_used

        try:
            guess = int(input(f"Attempt #{attempts_used} (Remaining: {remaining + 1}) - Enter guess: ").strip())
        except ValueError:
            print("  [Error] Please enter a valid integer.")
            attempts_used -= 1
            continue

        if guess == secret_number:
            print(f"\n[VICTORY] Congratulations! You guessed the number {secret_number} in {attempts_used} attempts!")
            return
        elif guess < secret_number:
            print("  Hint: Higher! Try a larger number.")
        else:
            print("  Hint: Lower! Try a smaller number.")

    print(f"\n[GAME OVER] You ran out of attempts! The secret number was {secret_number}.")


if __name__ == "__main__":
    play_game()
