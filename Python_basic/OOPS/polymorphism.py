"""polymorphism  """
# demonstrate polymorphism by defined a method fuel types in both car and electric car classes, but with different behaviors
# 
 
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Encapsulated (Private) attribute
        self.model = model

    # Getter method to read the private brand
    def get_brand(self):
        return self.__brand
    #polymorphism same method 
    def fuel_type(self):
        return "petrol or Diesel"

    # Setter method to safely modify the private brand
    def set_brand(self, new_brand):
        if isinstance(new_brand, str) and new_brand.strip() != "":
            self.__brand = new_brand
        else:
            print("Error: Invalid brand name!")

    def full_name(self):
        return f"{self.get_brand()} {self.model}"


""" Inheritance """
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
     #polymorphism same method 
    def fuel_type(self):
        return "electrical charge "

    def get_electric_details(self):
        return f"{self.get_brand()} {self.model} with {self.battery_size}"


# --- Demonstration ---

# Create a regular car
my_car = Car("Toyota", "Corolla")
print(my_car.get_brand())      # Prints: Toyota

# Change the brand using the setter
my_car.set_brand("Lexus")
print(my_car.get_brand())      # Prints: Lexus

# Test the validation logic
my_car.set_brand("")           # Prints: Error: Invalid brand name!


# Create an Electric Car
my_ev = ElectricCar("Tata", "Sierra", "89kWh")

# Change the EV brand using the inherited setter
my_ev.set_brand("Tesla")
print(my_ev.get_electric_details()) 

print(my_ev.fuel_type()) # Prints: Tesla Sierra with 89kWh

print(my_car.fuel_type())