""" Python Data Types 
    
    data types manje variable madhye konatya prakarcha data sathavla aahe he sangte.
    types of data types:
    1. integer - whole number 
    2. float  - decimal number
    3. string - text data and character data
    4. boolean - true or false values
    5. list - collection of data
    6. dictionary - collection of data in key value pair
    7. tuble - collection of data in ordered and unchangeable form
    8. set - collection of data in unordered and unchangeable form

"""
#interger data types 



# integer data types 

age=10
print("data type of age is ",age,type(age))

#float data types 

marks=90.4
print("data type of marks is ",marks,type(marks))


#string data types

name="Bharat"
print("data type of name is ",name,type(name))

#integer data types 
print("value of the zero")
value=0
print("data type of value is ",value,type(value))


#boolean data types 


is_student=False
print("data type of is_student is ",is_student,type(is_student))

# dictionary data types

student = {
    "name": "Bharat",
    "age": 21,
    "cgpa": 8.5
}

print("name:",student["name"])
print("data type of student is ",student,type(student))
#listdatatype
student_list=["Bharat",23,8.3]
print("data type of student_list is ",student_list,type(student_list))
print("name:",student_list[0])
print("age:",student_list[1])       
print("cgpa:",student_list[2])

# tuble data types
student_tuple=("Scahin",23,8.3) 
print("data type of student_tuple is ",student_tuple,type(student_tuple))
print("name:",student_tuple[0]) 
print("age:",student_tuple[1])
print("cgpa:",student_tuple[2])
