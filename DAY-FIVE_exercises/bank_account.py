# main.py

from bank_account import BankAccount

# Create an account
acct = BankAccount("Alice", 100.0)

# Deposit money
acct.deposit(50.0)

# Withdraw money
acct.withdraw(30.0)

# Check balance
print(f"Final balance: {acct.balance}")