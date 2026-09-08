
from decimal import Decimal
class Account:
    """A class that represents a bank account."""

    def __init__(self, name, balance):
        """Initialize the account with a name and balance."""
        if balance < Decimal('0.00'):
            raise ValueError("Balance cannot be negative")
        self.name = name
        self.balance = balance

    def deposit(self, amount: float):
        """Deposit money to the account."""
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount: float):
        """Withdraw an amount from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds or invalid amount")
    