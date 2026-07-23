# Polymorphism 
# overriding method 

class Parent():
    def sound(self):
        print('parent work')

class Child(Parent):
    def sound(self):
        print("child work")
        
    def sound(self,name):
        print(name)
        

obj=Child()
obj.sound('bharat')
# obj.sound()


# overloading method 

class Calculator:
    def add(self,a,b,c=0):
        result=a+b+c
        print(result)
        
obj=Calculator()
obj.add(10,30)
obj.add(12,21,30)