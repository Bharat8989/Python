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


class Student:
    college = "ABC College"  # Class Variable (Shared by all)

    def __init__(self, name):
        self.name = name     # Instance Variable (Unique to each)

s1 = Student("Bharat")
s2 = Student("Amit")

print(s1.name, s1.college)  # Output: Bharat ABC College
print(s2.name, s2.college)  # Output: Amit ABC College
