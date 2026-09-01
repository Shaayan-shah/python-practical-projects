"""
ATM Simulator & Account Management System
A clean, object-oriented command-line ATM simulator supporting PIN authentication,
balance inquiries, cash deposits, withdrawals, and transaction statements.
"""

from datetime import datetime
from typing import List, Dict, Any


class BankAccount:
    """Represents a bank account with transaction history and balance controls."""

    def __init__(self, account_number: str, holder_name: str, pin: str, initial_balance: float = 1000.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self._pin = pin
        self.balance = float(initial_balance)
        self.transactions: List[Dict[str, Any]] = []
        self._record_transaction("OPENING_BALANCE", initial_balance, "Account opened")

    def verify_pin(self, input_pin: str) -> bool:
        """Verify user PIN securely."""
        return self._pin == input_pin.strip()

    def get_balance(self) -> float:
        """Return current available balance."""
        return self.balance

    def deposit(self, amount: float) -> bool:
        """Deposit funds into the account."""
        if amount <= 0:
            print("[Error] Deposit amount must be greater than zero.")
            return False
        self.balance += amount
        self._record_transaction("DEPOSIT", amount, f"Deposited ${amount:,.2f}")
        print(f"[Success] Successfully deposited ${amount:,.2f}. Current balance: ${self.balance:,.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        """Withdraw funds with overdraft protection."""
        if amount <= 0:
            print("[Error] Withdrawal amount must be greater than zero.")
            return False
        if amount > self.balance:
            print(f"[Error] Insufficient funds. Available balance: ${self.balance:,.2f}")
            return False
        self.balance -= amount
        self._record_transaction("WITHDRAWAL", -amount, f"Withdrew ${amount:,.2f}")
        print(f"[Success] Successfully withdrew ${amount:,.2f}. Remaining balance: ${self.balance:,.2f}")
        return True

    def _record_transaction(self, tx_type: str, amount: float, description: str):
        """Internal helper to append transaction log entry."""
        self.transactions.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": tx_type,
            "amount": amount,
            "balance": self.balance,
            "description": description
        })

    def print_statement(self):
        """Print a formatted account statement."""
        print("\n" + "=" * 60)
        print(f"               ACCOUNT STATEMENT - {self.holder_name.upper()}")
        print(f" Account Number: {self.account_number} | Balance: ${self.balance:,.2f}")
        print("-" * 60)
        print(f" {'Date & Time':<20} | {'Type':<12} | {'Amount':<10} | {'Balance'}")
        print("-" * 60)
        for tx in self.transactions:
            amt_str = f"${abs(tx['amount']):,.2f}"
            sign = "+" if tx['amount'] >= 0 else "-"
            print(f" {tx['timestamp']:<20} | {tx['type']:<12} | {sign}{amt_str:<9} | ${tx['balance']:,.2f}")
        print("=" * 60 + "\n")


def main():
    account = BankAccount(account_number="PK-2026-9841", holder_name="Shayan Shah", pin="1234", initial_balance=5000.0)

    print("==================================================")
    print("           WELCOME TO APEX DIGITAL ATM            ")
    print("==================================================")

    max_attempts = 3
    is_authenticated = False

    for attempt in range(1, max_attempts + 1):
        entered_pin = input("Please enter your 4-digit PIN: ").strip()
        if account.verify_pin(entered_pin):
            is_authenticated = True
            break
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"[Incorrect PIN] {remaining} attempt(s) remaining.")
        else:
            print("[Locked] Maximum PIN attempts exceeded. Card retained for security.")
            return

    if not is_authenticated:
        return

    print(f"\nWelcome back, {account.holder_name}!")

    while True:
        print("\n--- Main Menu ---")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Print Mini Statement")
        print("5. Exit")

        choice = input("\nPlease select an option (1-5): ").strip()

        if choice == "1":
            print(f"\n[Balance Inquiry] Available Balance: ${account.get_balance():,.2f}")
        elif choice == "2":
            try:
                deposit_amt = float(input("Enter amount to deposit: $").strip())
                account.deposit(deposit_amt)
            except ValueError:
                print("[Error] Please enter a valid numerical amount.")
        elif choice == "3":
            try:
                withdraw_amt = float(input("Enter amount to withdraw: $").strip())
                account.withdraw(withdraw_amt)
            except ValueError:
                print("[Error] Please enter a valid numerical amount.")
        elif choice == "4":
            account.print_statement()
        elif choice == "5":
            print("\nThank you for choosing Apex Digital ATM. Goodbye!")
            break
        else:
            print("[Error] Invalid selection. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
