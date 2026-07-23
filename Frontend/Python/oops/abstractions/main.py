#  abstraction is a process of hiding the implementation detail from the user  only the highlighted set of service provided to the 



# import add,sub

# print("this for add")
# add.add()
# print("this for the sub")
# sub.sub()

from abc import ABC, abstractmethod


class CalculatorOperation(ABC):
    
    @abstractmethod
    def calculate(self):
        pass  

class Addition(CalculatorOperation):
    def calculate(self):
        a = int(input('enter first number:'))
        b = int(input('enter second number:'))
        print("adding of two numbers:", a + b)

class Subtraction(CalculatorOperation):
    def calculate(self):
        a = int(input('enter first number:'))
        b = int(input('enter second number:'))
        print("subtraction of two numbers:", a - b)


op1 = Addition()
op1.calculate() 

op2 = Subtraction()
op2.calculate()  