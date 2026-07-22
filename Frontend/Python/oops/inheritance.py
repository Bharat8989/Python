class Parent:
    
    def __init__(self, name):
        #instance attribute 
        self.name=name
        
    # instance method 
    def show_name(self):
        print(self.name)
        return self.name
        
    
class Child(Parent):
    def show_age(self,age):
        print(age)
        self.age=age
        print(self.age)
        
obj=Child('bharat')
obj.show_name()
obj.show_age(23)