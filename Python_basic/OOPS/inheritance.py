"""Inheritance  """
#problem :create an electric car class that inherits form the car class and has an additional attribute battery_size.

class Car:
    def __init__(self, brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"
    

# class and object 
my_car=Car("toyota ", "corolla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())

#inheritances 
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def full_nameEV(self):
        return f"{self.brand} {self.model} {self.battery_size}"
my_EV_car=ElectricCar("tataEv","sierra","89kWh")
print(my_EV_car.battery_size)

# print(my_EV_car.brand)
print(my_EV_car.full_nameEV())
print(my_EV_car.full_name())


print(my_EV_car.model)

print(my_car.full_name())