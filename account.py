import csv
import os.path

class Account:
    def __init__(self,account_id=int,balance=0,date=None,owner=None):
        
        self.account_id = account_id 
        if int(balance) >= 0:
            self.balance = int(balance)
        else:
            raise Exception ("Negative balance")
        self.date = date
        self.owner = self._import_owner()

    def owner_change(self,owner):
        self.owner = owner    

    def withdraw(self,money_to_withdraw):
        new_balance = self.balance - money_to_withdraw 
        if new_balance < 0:
            print("not enough balance to withdraw")
            return self.balance
        self.balance -= money_to_withdraw

    def deposit(self, money_to_deposit):
        self.balance = self.balance + money_to_deposit 
        return self.balance
    
    def get_balance(self):
        return f"{self.account_id} Your balance is {self.balance}"

    @classmethod
    def all_accounts(cls):
        accounts = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/accounts.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            reader.fieldnames= "account_id", "balance", "date"
            for row in reader:
                accounts.append(Account(**dict(row)))
        return accounts
    
    def _import_owner(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/account_owners.csv")
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == self.account_id:
                    return row[1]
    @classmethod
    def find(self,id):
        for account in self.all_accounts():
            if account.account_id == id:
                return account
    
    