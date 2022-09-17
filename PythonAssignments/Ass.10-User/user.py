
class user:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def make_deposite(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_balance(self):
        print (f"The balance of {self.name} is: {self.balance}")

    def make_transfer(self, receiver, amount):
        self.make_withdrawal(amount)
        receiver.make_deposite(amount)

user1 = user ("Osama Tbaileh", 5000)
user2 = user ("Hasan Sadaqa", 6000)
user3 = user ("Ziayd Qasem", 7000)

user1.make_deposite(100)
user1.make_deposite(100)
user1.make_withdrawal(100)
user1.display_balance()

user2.make_deposite(100)
user2.make_deposite(100)
user2.make_withdrawal(50)
user2.make_withdrawal(50)
user2.display_balance()

user3.make_deposite(100)
user3.make_withdrawal(50)
user3.make_withdrawal(50)
user3.make_withdrawal(50)
user3.display_balance()

user1.make_transfer(user3, 500)
user1.display_balance()
user3.display_balance()