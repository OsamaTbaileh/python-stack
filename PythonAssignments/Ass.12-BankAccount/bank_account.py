
class BankAccount:
    def __init__(self, name, balance=0, int_rate=0.01):
        self.name = name
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
        print(f"The balance in {self.name} account is: {self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print(f"Opreration failed - No enough balance in your account")
        return self

account_1 = BankAccount ("Osama Tbaileh", 1000)
account_2 = BankAccount ("Hasan Sadaqa", 2000)

account_1.make_deposite(100) .make_deposite(200) .make_deposite(
        300) .make_withdrawal(300) .yield_interest() .diplay_account_info()
        
account_2.make_deposite(200) .make_deposite(200) .make_withdrawal(
        50) .make_withdrawal(50) .make_withdrawal(50) .make_withdrawal(
        50) .yield_interest() .diplay_account_info()

