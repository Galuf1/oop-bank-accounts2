from account import Account
import csv
import os

class Owner:
    def __init__(self, owner_id= None, last_name= None, first_name= None, street_address= None, city= None, state= None, account_id=None):
        self.owner_id = owner_id
        self.last_name = last_name
        self.first_name = first_name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.account_id = account_id


    @classmethod
    def all_owners(self):
        owners = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/owners.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            reader.fieldnames= "owner_id", "last_name", "first_name", "street_address", "city", "state"
            for row in reader:
                new_var = Owner(**dict(row))
                owners.append(new_var)
        # for account in accounts:
        #     print(account.account_id, account.balance, account.date)
        return owners
    



        