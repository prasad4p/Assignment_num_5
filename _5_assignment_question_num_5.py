# Assignment_number_5
# Question_number_5 = Challenge 5: Handling a Bank Account.

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
        
    def withdrawal(self, amount):
        if amount < self.balance:
            balance = self.balance - amount
            print("Amount has been withdrawl successfully")
            print("Availabe Balnace = ", balance )
        else:
             print("Insufficient Balance")
    
    def deposit(self,amount):
         balance = self.balance + amount
         print("Amount has been Depsited")
         print("Availabe Balance = ", balance)

    def getBalance(self):
         return self.balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
            super().__init__(title, balance)
            self.interestRate = interestRate
    def interestAmount(self):
         return (self.interestRate * self.balance)/100
    
object_1 = Account ("Prasad", 5000)
print(object_1.title)
print(object_1.getBalance())
print(object_1.deposit(1000))
print(object_1.withdrawal(500))

object_2 = SavingsAccount("Prasad",5000,5)
print(object_2.title)
print(object_2.getBalance())
print(object_2.interestAmount())


