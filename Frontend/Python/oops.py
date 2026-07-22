# class Fruit:
#     def __init__(self,name,age):
#         self.student_name=name
#         self.student_age=age
#         # print(name)
#         # print(age)
        
#     def display(self,data):
#         self.data=data
       
#         print(self.student_name)
#         print(self.student_age)
#         print(data)
    
# f=Fruit('bharat',23)

# f.display("hello")
# Fruit('pavan',21).display('print')
# ff.display('world')






# aata norma class bg 

# class Fruit1:
#     name='pavan'
#     def info(name):
#         print(name)

# f1=Fruit1()
# f1.info()


class Student:
    school_name="government collage of engineering chandrapur"  # this is for the class attribute 
    namechange='pavan'
    def __init__(self,name):
        self.name1=name  # this is call the instance attribute 
        # print(f'my name is {name1} and school name is :{self.school_name}')
        print(self.name1)
        print(self.school_name)
        print(self.namechange)
        
s=Student('bharat')

s.school_name='ksk collage'
print(s.school_name)
s.namechange='pooja'

print(s.namechange)

