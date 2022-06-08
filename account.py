import csv
import os.path

class Account():
    def __init__(self,account_id=None,balance=None,date=None,owner=None):
        
        self.account_id = account_id 
        if int(balance) >= 0:
            self.balance = int(balance)
        else:
            raise Exception ("Negative balance")
        self.date = date
        self.owner = owner

    def owner_change(self,owner):
        self.owner = owner    

    def withdraw(self,money_to_withdraw):
        if self.balance == 0:
            raise Exception ("Balance is 0")
        new_balance = self.balance - money_to_withdraw 
        if new_balance > 0:
            return self.balance
        else:
            raise Exception ("Not enough balance")

    def deposit(self, money_to_deposit):
        self.balance = self.balance + money_to_deposit 
        return self.balance
    
    def get_balance(self):
        print(f"{self.id} Your balance is {self.balance}")

    @classmethod
    def all_accounts(self):
        accounts = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/accounts.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            reader.fieldnames= "account_id", "balance", "date"
            for row in reader:
                new_var = Account(**dict(row))
                accounts.append(new_var)
        # for account in accounts:
        #     print(account.account_id, account.balance, account.date)
        return accounts
    
    @classmethod
    def find(self,id):
        for account in self.all_accounts():
            if account.account_id == id:
                return account
