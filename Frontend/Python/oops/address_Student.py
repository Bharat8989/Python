class Address:
    def __init__(self, current_location, home_location, job_location):
        self.current_location = current_location
        self.home_location = home_location
        self.job_location = job_location


class Student:
    def __init__(self, student_id, name, age, salary, address_obj):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address_obj  # Integrates the Address class

    def display_details(self):
        print(f"--- Student Details ---")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: ${self.salary:,}")
        print(f"Current Location: {self.address.current_location}")
        print(f"Home Location: {self.address.home_location}")
        print(f"Job Location: {self.address.job_location}")


# --- Execution Example ---
# 1. Create an address object
student_address = Address("New York", "Los Angeles", "San Francisco")

# 2. Create a student object and pass the address object into it
student1 = Student(101, "Alice Smith", 21, 50000, student_address)

# 3. Display the information
student1.display_details()
