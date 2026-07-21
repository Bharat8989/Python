class Student:
    def __init__(self, student_id, name, student_class, age, marks):
        """
        Constructor method to initialize student attributes.
        """
        self.id = student_id          # Unique identification number
        self.name = name              # Student's name
        self.student_class = student_class  # Class/Grade (e.g., "10th", "12th")
        self.age = age                # Student's age
        self.marks = marks            # List or single integer for marks

    def display_details(self):
        """
        Instance method to print individual student details.
        """
        print(f"ID: {self.id} | Name: {self.name} | Class: {self.student_class} | Age: {self.age} | Marks: {self.marks}")


class StudentDatabase:
    def __init__(self):
        """
        Initializes an empty list to store Student objects.
        """
        self.students_list = []

    def add_student(self, student_id, name, student_class, age, marks):
        """
        Creates a new Student object and appends it to the linear list structure.
        """
        new_student = Student(student_id, name, student_class, age, marks)
        self.students_list.append(new_student)
        print(f"✅ Student '{name}' added successfully!")

    def display_all_students(self):
        """
        Loops through the list to print all records.
        """
        if not self.students_list:
            print("⚠️ The database is currently empty.")
            return
        
        print("\n--- Current Student Records ---")
        for student in self.students_list:
            student.display_details()

    def find_student_by_id(self, search_id):
        """
        Linear search function to find a student using their unique ID.
        """
        for student in self.students_list:
            if student.id == search_id:
                return student
        return None


# --- Running the Code ---

# 1. Instantiate the database structure
db = StudentDatabase()

# 2. Add new students to the list
db.add_student(student_id=101, name="Rahul", student_class="10th", age=15, marks=85)
db.add_student(student_id=102, name="Priya", student_class="12th", age=17, marks=92)
db.add_student(student_id=103, name="Amit", student_class="10th", age=16, marks=78)

# 3. Display the entire list
db.display_all_students()

# 4. Search for a specific student profile
search_target = 102
print(f"\n🔍 Searching for Student ID {search_target}...")
found_student = db.find_student_by_id(search_target)

if found_student:
    print("✨ Record Found:")
    found_student.display_details()
else:
    print("❌ Student profile not found.")


