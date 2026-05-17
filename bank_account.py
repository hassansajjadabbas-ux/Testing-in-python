
class BankAccount:
    def __init__(self,initial_balance = 0):
        self.balance = initial_balance
        self.transaction = []
        
    def deposit(self,amount : float) -> float:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance+=amount
        self.transaction.append(f'Depositing {amount}')
        return self.balance
    
    def withdraw(self,amount):
        if 0 < amount<=self.balance:
            self.balance-=amount
            self.transaction.append(f'Withdrawing {amount}')
            return self.balance
    
    def get_balance(self):
        return self.balance