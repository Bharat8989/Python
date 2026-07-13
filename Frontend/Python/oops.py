# class blueprint or template
# object is physical instance create from that blueprint


# class Student:
#     print('hello from the class')

    
# s1=Student()  # object creation
# Student()\
    
    
# class Student:
#     name='bharat'
    
#     def hello(self):
#         print('hello from the class')
        
# # Student()

# Student().hello()


# class Student:
#     college = "ABC College"  # Class Variable (Shared by all)

#     def __init__(self, name):
#         self.name = name     # Instance Variable (Unique to each)

# s1 = Student("Bharat")
# s2 = Student("Amit")

# print(s1.name, s1.college)  # Output: Bharat ABC College
# print(s2.name, s2.college)  # Output: Amit ABC College



# class Student:
#     name='Bharat'
#     age=22
    
#     def desc(self):
#         print(f'my name is ,{self.name} and i am , {self.age}, years odl')

# obj=Student()
# obj.desc()

# json stand for javaScript object notation . it is a built in package provide in python that is used to store and exchange data

import json

# json string 

colors = '["Red", "Yellow", "Green", "Blue"]'
lst1=json.loads(colors)
print(lst1)


colors1 = ["Red", "Yellow", "Green", "Blue"]

lst2=json.dumps(colors1)
print(lst2)
