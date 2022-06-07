from distutils.command.build_scripts import first_line_re
from owner import Owner


class Bank:
    def __init__(self):
        # self.account = Account.objects()
        pass

class Account():
    def __init__(self,account_id,balance,owner=None):
        
        self.account_id = account_id 
        if balance >= 0:
            self.balance = balance
        else:
            raise Exception ("Negative balance")
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

    
    

Banco = Bank()
Chris = Owner(121212,"ds","Chris","fsf","awdad","safsdf")
Chris_account = Account(121212,100) 
# Daniel = Account(63453,90)
print(Chris.first_name)
print(Chris_account.owner)
Chris_account.owner_change(Chris)
print(Chris_account.owner.first_name)

# Daniel.withdraw(10)
# print(Chris.id)
# print(Chris.balance)
# print(Daniel.balance)
# Chris.withdraw(100)
# print(Chris.balance)
# Chris.deposit(1000)
# print(Chris.balance)
# Chris.get_balance()


