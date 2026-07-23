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


# class Student:
#     school_name="government collage of engineering chandrapur"  # this is for the class attribute 
#     namechange='pavan'
#     def __init__(self,name):
#         self.name1=name  # this is call the instance attribute 
#         # print(f'my name is {name1} and school name is :{self.school_name}')
#         print(self.name1)
#         print(self.school_name)
#         print(self.namechange)
        
# s=Student('bharat')

# s.school_name='ksk collage'
# print(s.name1)
# print(s.school_name)
# s.namechange='pooja'

# print(s.namechange)



# types of method 
# there three types of method 
# 1 instance method 
# 2 class method @classmethod 
# 3 static method @staticmethod 




class Student:
    # class attribute 
    collageName='government collage of engineering chandrapur '
    def __init__(self, name,age):
        #instances attribute
        self.name=name
        self.age=age
        
    #instance method 
    
    def show_list(self):
        print('your name is :',self.name)
        print(f'my age is :{self.age}')
        print('my collage name is :',self.collageName)


    @classmethod
    def update_college(cls):
        cls.collageName='ksk college'
        return cls.collageName
    
    
    @staticmethod
    def student_marks(age):
        if age >= 18:
            return "adult"
        else:
            return "non-adult"
 
print('this is instance method ')       
s=Student('bharat',23)
        
print(s.show_list())
print("this is class method ")
update_collegeName=Student.update_college()
print(update_collegeName)

print(s.show_list())

print('this is static method ')

print(s.student_marks(40))

# print(s.age)



class Bharat:
    collageName="ksk college"
    def __init__(self,name,rollNo):
        self.name=name
        self.rollNo=rollNo
        
        
        
    def display(self):
        print(self.collageName) 
        print(Bharat.collageName)
        print(self.name)
        print(self.rollNo)

        
# Bharat("pavan",12)
obj=Bharat("pavan",12)
# obj=Bharat("pavan",12)
# obj.collageName="GCOEC"
obj.display()


# Bharat.display()
# Bharat('pavan,1')
# Bharat('pavan,1')