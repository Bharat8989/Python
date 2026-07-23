from datetime import datetime
Students = [
    {
        "id": 1, 
        "name": "Bharat",
        "date_of_birth": "2003-05-12",
        "marks": 85,
        "weight": 62.5
     },
    
    { 
        "id": 2, 
        "name": "Rahul", 
        "date_of_birth": "2004-08-22",
        "marks": 78,
        "weight": 65.0
     },
    
    {
        "id": 3,
        "name": "datta",
        "date_of_birth": "2003-11-05",
        "marks": 92,
        "weight": 52.3
    },
    
    {
        "id": 4,
        "name": "Amit",
        "date_of_birth": "2002-04-17",
        "marks": 64,
        "weight": 70.1
    },
    
    {
        "id": 5,
        "name": "pavan",
        "date_of_birth": "2004-01-30",
        "marks": 89,
        "weight": 55.8
    },
    {
        "id": 6,
        "name": "Rohit",
        "date_of_birth": "2003-09-14",
        "marks": 73,
        "weight": 68.4
    },
    {
        "id": 7,
        "name": "Suraj",
        "date_of_birth": "2003-03-25",
        "marks": 95,
        "weight": 50.0
    },
    {
        "id": 8,
        "name": "Vikram",
        "date_of_birth": "2002-07-09",
        "marks": 81,
        "weight": 74.2
    },
    {
        "id": 9,
        "name": "Pooja",
        "date_of_birth": "2004-06-11",
        "marks": 70,
        "weight": 58.1
    },
    {
        "id": 10,
        "name": "Chetan",
        "date_of_birth": "2003-12-03",
        "marks": 87,
        "weight": 66.9
    }
]


def display():
    print("all students list:",Students)
    
display()




def sumOfAllMarks():
    print('Sum of All Students Marks:')
    total=0
    for student in Students:
        total=total+student["marks"]
    return total

total_marks = sumOfAllMarks()
print(f"total_marks :{total_marks} ")
# 

# average student marks 

print("average students marks:", total_marks / len(Students))


def sumOfAllWeight():
    print('Sum of All Students Weight:')
    total=0
    for i in Students:
        total=total+i["weight"]
    return total

total_weight = sumOfAllWeight()
print(f"total_Weight :{total_weight} ")

# max and min marks 

#  pass a variable x to represend a student , and return x[marks]
def MaxAndMin(x):
    return x["marks"]
    
    
highest_student=max(Students,key=MaxAndMin)
lowest_student=min(Students, key=MaxAndMin)
print("finding highest and lowest marks :")
# max marks 
print(f"name : {highest_student['name']} | highest_marks: {highest_student['marks']}")

#  min marks 
print(f'name:{lowest_student['name']}  | lowest_marks:{lowest_student['marks']}')





# calculate age 

# def calculateAge():
#     current_year=datetime.now().year
#     for student in Students:
#         birth_year=int(student['date_of_birth'][:4])
#         age=current_year-birth_year
#         print(f'{student['name']}:{age} year')
        
# calculateAge()



def calculateAge():
    today = datetime.today()

    for student in Students:
        birth_date = datetime.strptime(
            student["date_of_birth"],
            "%Y-%m-%d"
        ).date()

        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        if days < 0:
            months -= 1

            previous_month = today.month - 1

            if previous_month == 0:
                previous_month = 12
                previous_year = today.year - 1
            else:
                previous_year = today.year
            days_in_previous_month = (
                datetime(previous_year, previous_month + 1, 1)
                - datetime(previous_year, previous_month, 1)
            ).days if previous_month != 12 else 31

            days += days_in_previous_month

        if months < 0:
            years -= 1
            months += 12

        if (today.month, today.day) < (birth_date.month, birth_date.day):
            years -= 1
            
            
        print(
            f"{student['name']}: "
            f"{years} years, {months} months, and {days} days"
        )


calculateAge()
