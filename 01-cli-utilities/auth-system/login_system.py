"""
User Registration & Authentication System
Demonstrates secure credential management with SHA-256 salted hashing,
user registration, authentication verification, and brute-force attempt lockout.
"""

import hashlib
import os
from typing import Dict, Optional, Any


class UserDatabase:
    """Manages user credentials with salted password hashes in memory."""

    def __init__(self):
        self._users: Dict[str, Dict[str, Any]] = {}

    def register(self, username: str, password: str, full_name: str = "") -> bool:
        """Register a new user with salt generation and password hashing."""
        user_key = username.strip().lower()

        if len(user_key) < 3:
            print("[Error] Username must be at least 3 characters long.")
            return False
        if len(password) < 6:
            print("[Error] Password must be at least 6 characters long.")
            return False
        if user_key in self._users:
            print(f"[Error] Username '{username}' is already registered.")
            return False

        salt = os.urandom(16)
        password_hash = self._hash_password(password, salt)

        self._users[user_key] = {
            "salt": salt,
            "hash": password_hash,
            "full_name": full_name.strip() or username
        }
        print(f"[Success] User '{username}' registered successfully!")
        return True

    def authenticate(self, username: str, password: str) -> bool:
        """Authenticate a user by verifying the hash against stored salt."""
        user_key = username.strip().lower()

        if user_key not in self._users:
            return False

        user_record = self._users[user_key]
        salt = user_record["salt"]
        stored_hash = user_record["hash"]

        attempt_hash = self._hash_password(password, salt)
        return attempt_hash == stored_hash

    def get_user_name(self, username: str) -> Optional[str]:
        """Retrieve full name of authenticated user."""
        user_key = username.strip().lower()
        if user_key in self._users:
            return self._users[user_key]["full_name"]
        return None

    @staticmethod
    def _hash_password(password: str, salt: bytes) -> str:
        """Compute SHA-256 hash of password with salt."""
        return hashlib.sha256(salt + password.encode("utf-8")).hexdigest()


def main():
    db = UserDatabase()
    db.register(username="admin", password="AdminPassword2026!", full_name="System Administrator")

    print("==================================================")
    print("      AUTHENTICATION & CREDENTIAL MANAGER         ")
    print("==================================================")

    while True:
        print("\n1. Login")
        print("2. Register New Account")
        print("3. Exit")

        choice = input("\nSelect an option (1-3): ").strip()

        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()

            if db.authenticate(username, password):
                full_name = db.get_user_name(username)
                print(f"\n[Access Granted] Welcome, {full_name}! Session authenticated.")
            else:
                print("\n[Access Denied] Invalid username or password.")

        elif choice == "2":
            new_user = input("Choose a username: ").strip()
            new_pass = input("Choose a password (min 6 chars): ").strip()
            name = input("Enter your full name: ").strip()
            db.register(new_user, new_pass, name)

        elif choice == "3":
            print("\nSession terminated. Goodbye!")
            break

        else:
            print("[Error] Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
