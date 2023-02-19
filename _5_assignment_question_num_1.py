# Assignment_number_5
# Question_number_1 = Challenge 1: Square Numbers and Return Their Sum.

class Point:

    def __init__(self):
        self.x = int(input("Enter the First Number : "))
        self.y = int(input("Enter the Second Number : "))
        self.z = int(input("Enter the Third Number : "))

    def sqsum(self):
        number_1 = self.x ** 2
        number_2 = self.y ** 2
        number_3 = self.z ** 2
        sum = number_1 + number_2 + number_3
        
        print(f"Square of Number_1 : {number_1} \nSquare of Number_2 : {number_2} \nsquare of Number_3 : {number_3}")
        print("Sum of All Three Square Number : ",sum )

object = Point()
object.sqsum()


