# inheritance 


class Parent:
    def speak(self):
        print('i can speak')

        
class Child(Parent):
    print('this is parent class ')
    
obj=Child()
obj.speak()

