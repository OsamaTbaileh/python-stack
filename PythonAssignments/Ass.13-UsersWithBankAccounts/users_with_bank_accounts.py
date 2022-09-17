
class user:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()
    
    def deposite(self, amount):
        self.account.make_deposite(amount)
        return self

    def withdrawal(self, amount):
        self.account.make_withdrawal(amount)
        return self

    def displaybalance(self):
        print (f"The balance of {self.name} is: {self.account.balance}")
        # self.account.diplay_account_info()                         # # another staremnt 

    def make_transfer(self, receiver, amount):
        self.make_withdrawal(amount)
        receiver.make_deposite(amount)
        return self



class BankAccount:
    def __init__(self, balance=0, int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate

    def make_deposite(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.balance > 0:
            self.balance -= amount
        else:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def diplay_account_info(self):
        print(f"The balance in this account is: {self.balance}$")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print(f"Opreration failed - No enough balance in your account")
        return self


user1 = user ("Osama Tbaileh")
user2 = user ("Hasan Sadaqa")
user3 = user ("Ziayd Qasem")

user1.deposite(100).deposite(100).withdrawal(100).displaybalance()