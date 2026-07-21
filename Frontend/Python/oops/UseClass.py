from datetime import datetime

# 1. THE STUDENT BLUEPRINT (Individual Student Entity)
class Student:
    def __init__(self, id, name, date_of_birth, marks, weight):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.marks = marks
        self.weight = weight

    def get_age(self):
        current_year = datetime.now().year
        birth_year = int(self.date_of_birth[:4])
        return current_year - birth_year


# 2. THE CLASSROOM MANAGER (Handles all group operations)
class Classroom:
    def __init__(self):
        # We store the Student Objects inside this list
        self.students_list = []

    def add_student(self, student_obj):
        self.students_list.append(student_obj)

    def display_all(self):
        print("====== All Students List ======")
        for s in self.students_list:
            print(f"ID: {s.id} | Name: {s.name} | Marks: {s.marks} | Weight: {s.weight}kg")
        print("-" * 40)

    def sum_of_all_marks(self):
        total = 0
        for s in self.students_list:
            total += s.marks
        return total

    def calculate_average_marks(self):
        if not self.students_list:
            return 0
        return self.sum_of_all_marks() / len(self.students_list)

    def sum_of_all_weight(self):
        total = 0
        for s in self.students_list:
            total += s.weight
        return total

    def print_highest_and_lowest(self):
        print("====== Finding Highest and Lowest Marks ======")
        # Using lambda on Student objects directly via dot notation (.marks)
        highest = max(self.students_list, key=lambda s: s.marks)
        lowest = min(self.students_list, key=lambda s: s.marks)
        
        print(f"Max -> Name: {highest.name} | Marks: {highest.marks}")
        print(f"Min -> Name: {lowest.name} | Marks: {lowest.marks}")
        print("-" * 40)

    def print_all_ages(self):
        print("====== Detailed Age Calculations ======")
        for s in self.students_list:
            print(f"{s.name}: {s.get_age()} years old")
        print("-" * 40)


# --- EXECUTION (How to use it) ---

# 1. Instantiate the Classroom
my_class = Classroom()

# 2. Raw Data converting into Student Objects
raw_data = [
    {"id": 1, "name": "Bharat", "date_of_birth": "2003-05-12", "marks": 85, "weight": 62.5},
    {"id": 2, "name": "Rahul", "date_of_birth": "2004-08-22", "marks": 78, "weight": 65.0},
    {"id": 3, "name": "datta", "date_of_birth": "2003-11-05", "marks": 92, "weight": 52.3},
    {"id": 4, "name": "Amit", "date_of_birth": "2002-04-17", "marks": 64, "weight": 70.1},
    {"id": 5, "name": "pavan", "date_of_birth": "2004-01-30", "marks": 89, "weight": 55.8},
    {"id": 6, "name": "Rohit", "date_of_birth": "2003-09-14", "marks": 73, "weight": 68.4},
    {"id": 7, "name": "Suraj", "date_of_birth": "2003-03-25", "marks": 95, "weight": 50.0},
    {"id": 8, "name": "Vikram", "date_of_birth": "2002-07-09", "marks": 81, "weight": 74.2},
    {"id": 9, "name": "Pooja", "date_of_birth": "2004-06-11", "marks": 70, "weight": 58.1},
    {"id": 10, "name": "Chetan", "date_of_birth": "2003-12-03", "marks": 87, "weight": 66.9}
]

# Loading raw data into the Classroom Class as objects
for item in raw_data:
    student = Student(item["id"], item["name"], item["date_of_birth"], item["marks"], item["weight"])
    my_class.add_student(student)

# 3. Triggering calculations via class methods
my_class.display_all()

total_m = my_class.sum_of_all_marks()
print(f"Sum of All Students Marks: {total_m}")
print(f"Average Students Marks   : {my_class.calculate_average_marks():.2f}")

total_w = my_class.sum_of_all_weight()
print(f"Sum of All Students Weight: {total_w} kg")
print("-" * 40)

my_class.print_highest_and_lowest()
my_class.print_all_ages()
