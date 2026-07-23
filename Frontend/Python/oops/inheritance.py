# 
# class Parent:
    
#     def __init__(self, name):
#         #instance attribute 
#         self.name=name
        
#     # instance method 
#     def show_name(self):
#         print(self.name)
#         return self.name
        
    
# class Child(Parent):
#     def show_age(self,age):
#         print(age)
#         self.age=age
#         print(self.name)
#         print(name)
#         # print(self.age)
        
# obj=Child('bharat')
# obj.show_name()
# obj.show_age(23)

# Single inheritance  ---------------

class Parent:
    def cooking_gas(self):
        print("gas on ")
    
class Child(Parent):
    def make_tea(self):
        self.cooking_gas()
        print('your chai is ready ')

obj=Child()
obj.make_tea()
# obj.cooking_gas()


# multiple inheritances ----------

# class Mother:
#     def cooking_skill(self):
#         print("cooking skill")

# class Father:
#     def driving_skill(self):
#         print("driving skill")
        
        
# class Child(Mother, Father ):
#     def cricketing_skill(self):
#         self.cooking_skill()
#         self.driving_skill()
#         print('playing cricket well ')
        
        
# obj=Child()
# obj.cricketing_skill()


# Multilevel inheritances

class GrandFather:
    def __init__(self):
        self.surname='kadam'
        
    def land_property(self):
        print("property for the grand father ")

class Father(GrandFather):
    def business_skill(self):
        print('skill from father business management')

class Child(Father):
    def coding_skill(self):
        self.land_property()
        self.business_skill()
        print("son's own personal skill ")

obj=Child()

obj.coding_skill()

print("son's surname:",obj.surname)

print(obj)
# print(Child()) show the memory address use the __str__ method that not show the memory address show the object for the give functions 


