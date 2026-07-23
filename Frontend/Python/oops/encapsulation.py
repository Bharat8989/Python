# encapsulations 

class Demo:
    def __init__(self):
        self.name='public member'    #public 
        self._age=21                 #protected
        self.__salary=40000          #private
        
        
    def show(self):
        print('inside the class')
        print("public:",self.name)
        print('Protected',self._age)
        print('Private', self.__salary)
        
obj=Demo()
obj.show()
print(obj.name)
obj.name='pavan'
print(obj.name)
print(obj._age)
# print(obj.__salary)
print(obj._Demo__salary)
