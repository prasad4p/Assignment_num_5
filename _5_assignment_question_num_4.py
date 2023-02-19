# Assignment_number_5
# Question_number_4 = Challenge 4: Implement a Banking Account.

class Account:
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self,title,balance,interestrate):
        super().__init__(title,balance)
        self.interestrate = interestrate


object = SavingsAccount("Prasad", 5000, 5)
print(object.title)
print(object.balance)
print(object.interestrate)