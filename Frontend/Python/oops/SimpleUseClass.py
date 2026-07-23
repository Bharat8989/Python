from datetime import datetime

from dateutil.relativedelta import relativedelta 

class Student:

    raw_data = [
        { 'id' : 1, 'name' : 'Bharat' , 'date_of_birth' : '12-05-2003' , 'marks' : 85, 'weight' : 62.5 },
        { 'id' : 2, 'name' : 'Rahul' , 'date_of_birth' : '22-08-2004' , 'marks' : 78, 'weight' : 65.0 },
        { 'id' : 3, 'name' : 'datta' , 'date_of_birth' : '05-11-2003' , 'marks' : 92, 'weight' : 52.3 },
        { 'id' : 4, 'name' : 'Amit' , 'date_of_birth' : '17-04-2002' , 'marks' : 64, 'weight' : 70.1 },
        { 'id' : 5, 'name' : 'pavan' , 'date_of_birth' : '30-01-2004' , 'marks' : 89, 'weight' : 55.8 },
        { 'id' : 6, 'name' : 'Rohit' , 'date_of_birth' : '14-09-2003' , 'marks' : 73, 'weight' : 68.4 },
        { 'id' : 7, 'name' : 'Suraj' , 'date_of_birth' : '25-03-2003' , 'marks' : 95, 'weight' : 50.0 },
        { 'id' : 8, 'name' : 'Vikram' , 'date_of_birth' : '09-07-2002' , 'marks' : 81, 'weight' : 74.2 },
        { 'id' : 9, 'name' : 'Pooja' , 'date_of_birth' : '11-06-2004' , 'marks' : 70, 'weight' : 58.1 }
    ]

    def __init__(self, id, name, date_of_birth, marks, weight):
        date_obj = datetime.strptime(date_of_birth, "%Y-%m-%d") 
        standard_dob = date_obj.strftime("%d-%m-%Y")
  
        new_student = {
            "id": id,
            "name": name,
            "date_of_birth": standard_dob,
            "marks": marks,
            "weight": weight
        }

        Student.raw_data.append(new_student)

    def print_all_students(self):
        print("\n--- All Students inside raw_data ---")
        for student in Student.raw_data:
            print(f"ID: {student['id']}, Name: {student['name']}, Marks: {student['marks']}")
            print("--------------------")
    
    def filter_by_marks(self, min_marks):
        print(f"\n--- Students with Marks >= {min_marks} ---")
        for student in Student.raw_data:
            if student['marks'] >= min_marks:
                print(f'Name:{student["name"]}, marks:{student["marks"]}')

    def sum_of_marks(self):
        total = 0
        for student in Student.raw_data:
            total = total + student['marks']
        print(f"\nSum of all student marks: {total}")
        return total

    def average_of_marks(self):
        total = self.sum_of_marks() 
        total_students = len(Student.raw_data)
        average = total / total_students
        print(f"Average of All Student Marks: {round(average, 2)}")
        print("--------------------")

    def min_max_marks(self):
        print("\n--- Min & Max Marks Analysis ---")
        
        max_student = Student.raw_data[0]
        min_student = Student.raw_data[0]
        
        for student in Student.raw_data:
            if student['marks'] > max_student['marks']:
                max_student = student
            if student['marks'] < min_student['marks']:
                min_student = student
                
        print(f"Highest Marks: {max_student['name']} ({max_student['marks']} Marks)")
        print(f"Lowest Marks : {min_student['name']} ({min_student['marks']} Marks)")
        print("--------------------")

    # count year 
    # def countYear(self):
    #     print("\n--- Student Age Analysis (Years, Months, Days) ---")
        
        
    #     today = datetime.now()
        
    #     for student in Student.raw_data:
    #         dob_obj = datetime.strptime(student['date_of_birth'], "%d-%m-%Y")
            
           
    #         diff = today - dob_obj
            
           
    #         total_days = diff.days
    #         years = total_days // 365
    #         remaining_days = total_days % 365
    #         months = remaining_days // 30
    #         days = remaining_days % 30
            
           
    #         print(f"Name: {student['name']:<8} | Age: {years} Years, {months} Months, {days} Days")
            
    #     print("--------------------")

    def countYear(self):
        print("\n--- Student Age Analysis (Years, Months, Days) ---")
        today = datetime.now()
        for student in Student.raw_data:
            dob_obj = datetime.strptime(student['date_of_birth'], "%d-%m-%Y")
            diff = relativedelta(today, dob_obj)
            print(f"Name: {student['name']:<8} | Age: {diff.years} Years, {diff.months} Months, {diff.days} Days")
        print("--------------------")
        
    def nextBirthday(self):
        print("\n--- Next Birthday Analysis ---")
        today = datetime.now()
        
        for student in Student.raw_data:
            dob = datetime.strptime(student['date_of_birth'], "%d-%m-%Y")
            
            next_bday = datetime(today.year, dob.month, dob.day)
            
            if next_bday < today:
                next_bday = datetime(today.year + 1, dob.month, dob.day)
                
            days_left = (next_bday - today).days + 1
            
            print(f"Name: {student['name']:<8} | Next Birthday: {next_bday.strftime('%d-%m-%Y')} | Days Left: {days_left} Days")
        print("--------------------")


s1 = Student(10, "Karan", "2003-05-12", 85, 62.5)
s2 = Student(11, "Kiran", "2004-08-22", 78, 65.0)

s1.average_of_marks()
s1.min_max_marks()

s1.countYear()
