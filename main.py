from bank_account import BankAccount

balance = 100
account = BankAccount(initial_balance=balance)


print(f"initial balance {account.balance}")
print(f"Depositing 50 {account.deposit(amount=50)}")
print(f"Withdrawing 30 {account.withdraw(30)}")