# Assignment_number_5
# Question_number_3 = Challenge 3: Implement the Complete Student Class.

class Student:

    def __init__(self,_name,_roll_number):
        self._name = _name
        self._roll_number = _roll_number
        print(f"Name : {self._name} \nRoll Number : {self._roll_number}")

    def setName(self,name):
        self._name = name
        
    def getName(self):
        return self._name
    
    def setRollNumber(self,roll_number):
        self._roll_number = roll_number

    def getRollNumber(self):
        return self._roll_number
    
object = Student("Prasad" , 1)
print((object.getName()))
print((object.getRollNumber()))

