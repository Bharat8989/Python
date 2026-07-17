# class Student:
#     print("this class object ")
    
#     def home():
#         print('home page')
#     # home()
#     print(home)
        
# student =Student()


# print(type(student))


# student.name='rahul'
# student.age=20

# print(student)



# memory_address=id(data)
# print(memory_address)


# class Student:
#     def display(self,nav):
#         self.name=nav
        
#     def display1(self):
#         print('hello',self.name)
#     display()

# stu=Student()

# stu.display()


# method is function inside a class

# class Student:
#     def display(self):
#         print(self)
#         print("hello student")
        
#     # display()

        
# std=Student()
# std.display()
# std.display()


# class Student:
#     def __init__(self):
#         print('constructor called')

# obj1=Student()


#  creating multiple object 
# class Student:

#     def __init__(self, name, age, branch):

#         self.name = name
#         self.age = age
#         self.branch = branch

#     def display(self):

#         print("Name :", self.name)
#         print("Age :", self.age)
#         print("Branch :", self.branch)

# student1 = Student("Rahul", 20, "CSE")
# student2 = Student("Amit", 21, "IT")

# student1.display()

# print("----------------")

# student2.display()



# class Car:
#     brand='toyota'
#     species='dog'
#     print(brand)
    
#     def make_sound(self):
#         print(self.species)
#         print(self.brand)

# obj=Car()
# obj.make_sound()

# class Animal:
#     type='cat'
#     def sound(self):
#         print('meow')
    
# # print(Animal().type)
# obj=Animal()
# obj.sound()

class Student :
    def __init__(self,name):
        self.name=name     # instance attribute
        
obj=Student('bharat')

print(obj)
print(obj.name)

class MyClass:
    @classmethod
    def class_method(self):
        print('this is an instance method ')

obj=MyClass()
obj.class_method()

