# Password Strength Checker (with loop to try again)

print("=" * 40)
print("PASSWORD STRENGTH CHECKER")
print("=" * 40)

# Loop to check multiple passwords
while True:
    print("\n" + "-" * 40)
    password = input("Enter password (or type 'quit' to exit): ")
    
    # Exit condition
    if password == "quit":
        print("Goodbye!")
        break
    
    # Check criteria
    length_ok = len(password) >= 8
    has_number = False
    has_uppercase = False
    
    # Check for numbers
    for char in password:
        if char >= '0' and char <= '9':
            has_number = True
    
    # Check for uppercase letters
    for char in password:
        if char >= 'A' and char <= 'Z':
            has_uppercase = True
    
    # Calculate score
    score = 0
    if length_ok:
        score = score + 1
    if has_number:
        score = score + 1
    if has_uppercase:
        score = score + 1
    
    # Show results
    print("\n--- PASSWORD CHECK ---")
    print("Length (8+):", length_ok)
    print("Has number:", has_number)
    print("Has uppercase:", has_uppercase)
    print("Score:", score, "/ 3")
    
    # Give strength rating
    if score == 3:
        print("Strength: STRONG")
    elif score == 2:
        print("Strength: MEDIUM")
    else:
        print("Strength: WEAK")
    
    print("-" * 40)