from datetime import datetime

class Student:
    
    raw_data = []


    def __init__(self, id, name, date_of_birth, marks, weight):
        # Parses "YYYY-MM-DD" from your input argument
        date_obj = datetime.strptime(date_of_birth, "%d-%m-%Y") 
        
        
        standard_dob = date_obj.strftime("%d-%m-%Y")
        
       
        
        self.id=id
        self.name=name
        self.date_of_birth=standard_dob
        self.marks= marks
        self.weight= weight
        
       
        Student.raw_data.append(self)

    def printData(self):
        for student in Student.raw_data:
            print(f"ID : {student.id}, Name: {student.name}, DOB:{student.date_of_birth}")
            print("--------------------")
    
    def sumOfStudentMarks(self):
        total=0
        for student in Student.raw_data:
            total=total+student.marks
        print("\nsum of all student marks:",total)
        return total

    def averageMarks(self):
        total=self.sumOfStudentMarks()
        
        average= total / len(Student.raw_data)
        print("--------------")
        return print("Average of All Student Marks:",average)
       
    def totalWeight(self):         
            
            
      pass  
     
       

s1 = Student(1, "Bharat", "12-05-2003", 85, 62.5)
s2 = Student(2, "Rahul", "22-08-2004", 78, 65.0)
s3 = Student(3, "datta", "05-11-2003", 92, 52.3)
s4 = Student(4, "Amit", "17-04-2002", 64, 70.1)
s5 = Student(5, "pavan", "30-01-2004", 89, 55.8)
s6 = Student(6, "Rohit", "14-09-2003", 73, 68.4)
s7 = Student(7, "Suraj", "25-03-2003", 95, 50.0)
s8 = Student(8, "Vikram", "09-07-2002", 81, 74.2)
s9 = Student(9, "Pooja", "11-06-2004", 70, 58.1)


s1.printData()
s1.sumOfStudentMarks()
s1.averageMarks()
