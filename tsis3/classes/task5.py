#Create a bank account class that has attributes owner, balance and two methods deposit and withdraw. Withdrawals may not exceed the available balance. Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print("+deposit")

    def withdraw(self, money):
        if amount > self.balance:
            print("you're poor")
        else:
            self.balance -= money
            print("you can withdraw")