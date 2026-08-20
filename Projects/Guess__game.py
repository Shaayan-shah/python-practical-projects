"""
SIMPLE NUMBER GUESSING GAME
Basic version with difficulty levels
"""

import random

print("=" * 40)
print("🎮 NUMBER GUESSING GAME 🎮")
print("=" * 40)

# Ask for difficulty
print("\nDifficulty Levels:")
print("1. Easy (15 tries)")
print("2. Medium (10 tries)")
print("3. Hard (5 tries)")

choice = input("\nChoose difficulty (1/2/3): ")

# Set attempts based on difficulty
if choice == "1":
    attempts_left = 15
    print("\n🎯 EASY MODE - You have 15 attempts!")
elif choice == "2":
    attempts_left = 10
    print("\n🎯 MEDIUM MODE - You have 10 attempts!")
else:
    attempts_left = 5
    print("\n🎯 HARD MODE - You have 5 attempts!")

# Generate random number
secret = random.randint(1, 100)
attempts_used = 0

# Game loop
while attempts_left > 0:
    print(f"\nAttempts left: {attempts_left}")
    
    # Get guess
    guess = int(input("Guess a number (1-100): "))
    attempts_used = attempts_used + 1
    attempts_left = attempts_left - 1
    
    # Check guess
    if guess == secret:
        print(f"\n🎉 CORRECT! You got it in {attempts_used} tries!")
        break
    elif guess < secret:
        print("📈 Too low!")
    else:
        print("📉 Too high!")

# If game over without winning
if guess != secret:
    print(f"\n💀 GAME OVER! The number was {secret}")

print("\nThanks for playing!")