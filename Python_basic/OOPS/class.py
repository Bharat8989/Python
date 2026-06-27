"""class ha ek object tayar karnyathi blueprint asto"""
# class Student:
#     print("hello")
# # object 
# Student()
# s1=Student()
# s2=Student()

# class Car:
#     name="toyota"
# c1=Car()
# print(c1.name)

#method (class mathil function la method mahnatat)

# class Student:
#     def hello(self):
#         print("hello student")
# s1=Student()
# s1.hello() 
#what is self
#self represents the current object 
# class Student:
#     def hello(self):
#         print("hello student")
        
# s1=Student()
# s1.hello()

#constructor ( a constructor is a special method executed automatically when an object is created.)
# problem basic class and object
class Car:
    def __init__(self, brand,model):
        self.brand=brand
        self.model=model
    # def full_name(self):
    #     return f"{self.brand} {self.model}"
    

my_car=Car("Toyota","Corolla")
print((my_car.brand))
print(my_car.model)

my_new_car=Car("tata","safari")
print(my_new_car.brand)
print(my_new_car.model)