from argparse import ArgumentError
from types import new_class
from account import Account

class SavingsAccount(Account):
    def __init__(self, account_id, balance, date, owner=None):
        if balance < 1000:
            raise ArgumentError("Initial value has to be at least $10")
        else:
            super().__init__(account_id, balance, date, owner)
            self.fee = 200
            self.interest_rate = 0.25

    def withdraw(self, money_to_withdraw):
        new_balance = self.balance - money_to_withdraw
        if new_balance > 1200:
            self.balance -= (money_to_withdraw + self.fee)
        else:
            print(f"Must have over $10 plus fee ${self.fee} to withdraw")
        print(f"Current balance: {self.balance}")
    
    def add_interest(self):
        interest = self.balance * (self.interest_rate/100)
        self.balance += interest
        return interest