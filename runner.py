from bank import Bank
from account import Account
from owner import Owner

Daniel = Account(1212,1235667,"1999-03-27 11:30:09 -0800")
# print(Daniel.account_id)
# print(Daniel.balance)
# print(Daniel.date)
# print (Account.all_accounts())
find = Daniel.find("1213")
for owner in Owner.all_owners():
    print(Account.find("1213").account_id)
# print(Owner.all_owners())