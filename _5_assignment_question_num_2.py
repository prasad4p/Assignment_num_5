# Assignment_number_5
# Question_number_2 = Challenge 2: Implement a Calculator Class.

class Calculator:

    def __init__(self):
        self.number_1 = float(input("Enter the First Number : "))
        self.number_2 = float(input("Enter the Second Number : "))

    def add(self):
        addition = self.number_1 + self.number_2
        print("Addition of First NUmber and Second Number : ", addition)

    def subtract(self):
        subtraction = self.number_1 - self.number_2
        print("Subtraction of First Number and Second Number : ", subtraction)

    def multiply(self):
        multiplication = self.number_1 * self.number_2
        print("Multiplicatin of First Number and Second Number : ", multiplication)

    def divide(self):
        division = self.number_1 / self.number_2
        print("Division of First Number and Second Number : ", division)


obj = Calculator()
obj.add()
obj.subtract()
obj.multiply()
obj.divide()