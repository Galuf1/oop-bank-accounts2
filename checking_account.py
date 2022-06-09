from account import Account

class CheckingAccount(Account):
    def __init__(self,account_id, balance, date, owner=None):
        super().__init__(account_id,balance,date,owner)
        self.fee = 100
        self.checks = 0

    def withdraw(self, money_to_withdraw):
        amount = self.balance - money_to_withdraw - self.fee
        if amount > 0:
            self.balance -= (money_to_withdraw + self.fee)
        else:
            print(f"Not enough balance to withdraw")
            return self.balance
        
    def withdraw_using_check(self,money_to_withdraw):
        amount = self.balance - money_to_withdraw 
        if amount > -1000 and self.checks >= 3:
            self.balance -= (money_to_withdraw + 200)
            self.checks += 1
        if amount > -1000:
            self.balance -= money_to_withdraw
            self.checks += 1
        else:
            print("Not enough balance to withdraw") 
            return self.balance

    def reset_checks(self):
        self.checks = 0 

