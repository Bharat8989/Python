"""Static method """
# add a static method to the car class that return a general description of a car .
#not access instance variable 

# class Car:

#     @staticmethod
#     def description():
#         return "A car is a four-wheeled vehicle used for transportation."


# print(Car.description())
class Car:

    def __init__(self, brand):
        self.brand = brand

    @staticmethod
    def description():
        return "Cars are used for travelling."


car1 = Car("BMW")
car2 = Car("Audi")

print(car1.brand)
print(car2.brand)

print(Car.description())