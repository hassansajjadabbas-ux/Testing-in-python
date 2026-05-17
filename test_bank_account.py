from bank_account import BankAccount
import pytest
"python -m pytest test_bank_account.py"

@pytest.fixture
def account():
    balance = 100
    account = BankAccount(initial_balance=balance)
    return account


def test_initail_balance(account):
    """is the inital balance is equal 100"""
    assert account.balance == 100

def test_deposit(account):
    
    deposit = 50
    assert account.deposit(amount=deposit) == 150

def test_withdraw(account):
    
    withdraw = 50
    
    assert account.withdraw(amount=withdraw) == 50

def test_deposit_transaction(account):
   
    account.deposit(50)
    assert "Depositing 50" in account.transaction

def test_withdraw_transaction(account):
   
    account.withdraw(50)
    assert "Withdrawing 50" in account.transaction

def test_invalid_deposit(account):
    with pytest.raises(ValueError) as exc_info:
        account.deposit(amount=-11)

    assert str(exc_info.value ) == "Deposit must be positive"
@pytest.mark.parametrize("amount",[0,-20,-6,-30,-1])
def test_more_invaild_deposit(account,amount):
    with pytest.raises(ValueError):
        account.deposit(amount)
    

def test_invalid_withdraw(account):
   
    account.withdraw(amount=200)
    assert account.balance == 100

def test_get_balance(account):

    assert account.get_balance() == 100

    account.deposit(amount=200)
    assert account.get_balance() == 300

    account.withdraw(amount=30)
    assert account.get_balance() == 270
