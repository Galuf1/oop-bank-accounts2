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
        self.account_id = self._import_account()


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
        return owners

    def _import_account(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "support/account_owners.csv")
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[1] == self.owner_id:
                    return row[0]
    



        