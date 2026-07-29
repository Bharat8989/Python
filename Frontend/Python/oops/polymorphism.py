# # Polymorphism 
# # overriding method 

# class Parent():
#     def sound(self):
#         print('parent work')
#         # print(data)

# class Child(Parent):
#     def sound(self,data):
#         print("child work")
#         print(data)
        
   
        

# obj=Child()
# obj2=Parent()
# obj2.sound()
# obj.sound('bharat')

# # obj.sound()


# # overloading method


# # class Calculator:
# #     def add(self,a,b,c):
# #         result=a+b+c
# #         print(result)
        
# #     def add(self,a,b):
# #         result=a+b
# #         print(result)
        
# # obj=Calculator()
# # obj.add(10,30)
# # obj.add(12,21,30)


# class Calculator:
   
#     def add(self, a, b, c=0, d=0):
#         result = a + b + c + d
#         print(result)

# obj = Calculator()
# obj.add(10, 20)        
# obj.add(10, 20, 30)    
# obj.add(5, 5, 5, 5)    


# Duck typing method 

class Dog:
    def sound(self):
        return "don (bau-bau)"

class Cat:
    def sound(self):
        return "myau myam"

# create a functions 

def make_animal_sound(animal_object):
    print(animal_object.sound())

# crete a object for the both

motu=Dog()
mini=Cat()

make_animal_sound(motu)
make_animal_sound(mini)



# method overriding
print("method overriding")

# Parent Class
class Car:
    def drive(self):
        print('Driving safely at 60 km/h')

# Child Class inherits from Car
class SportsCar(Car):
    def drive(self):
        # use the super keyword 
        super().drive()
       
        print('Driving super fast at 200 km/h!')
        
# Creating an object of the Child Class
obj = SportsCar()
obj.drive()
# obj1=Car()
# obj1.drive()



# method overriding 

class Employee:
    def calculate_salary(self):
        return "This employee receives the base salary."

class Manager(Employee):
    # Overriding the parent method specifically for the Manager
    def calculate_salary(self):
        return "Base salary + Bonus will be provided."

class Developer(Employee):
    # Overriding the parent method specifically for the Developer
    def calculate_salary(self):
        return "Base salary + Overtime pay will be provided."

# How to use it:
staff = [Manager(), Developer()]

for person in staff:
    print(person.calculate_salary())






