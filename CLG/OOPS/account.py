from custom_account import Account
from decimal import Decimal

value = Decimal('12.34')
account1 = Account('John Green', Decimal('50.00'))

print(account1.name)
print(account1.balance)
account1.deposit(Decimal('20.00'))
print(account1.balance)
account1.withdraw(Decimal('10.00'))
print(account1.balance)