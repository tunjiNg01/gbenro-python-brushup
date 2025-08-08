# bank_account.py

class BankAccount:
    """A simple bank account with deposit and withdrawal."""

    def __init__(self, owner: str, starting_balance: float = 0.0):
        self.owner = owner
        self.balance = float(starting_balance)

    def deposit(self, amount: float):
        """Add money to the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount: float):
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

