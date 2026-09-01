# create account class with 2 attributes - balance & account no.
# create methods for debit, credit & printing the balance.

class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc

    # debit
    def debit(self,amount):
        self.balance-=amount
        print("Rs. ", amount,"was debited")
        print("Total balance= ",self.get_balance())

    # credit
    def credit(self,amount):
        self.balance+=amount
        print("Rs. ", amount,"was credited")
        print("Total balance= ",self.get_balance())

    # getbalance
    def get_balance(self):
        return self.balance

acc1=Account(10000,12345)
print(acc1.balance)
print(acc1.account)

acc1.debit(1000)
acc1.credit(500)
