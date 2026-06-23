# # """Sum of two Numbers"""
# # #using the user input 

# # # num1=int(input("enter the first number:"))
# # # num2=int(input("enter the second number :"))
# # # # num1=int(num1)
# # # sum =num1+num2
# # # #the valule of the give num1 and num2

# # # print("the num1 values is :",num1, "and num2 value is :",num2)

# # # print("the sum of the num1 and num2 is :",sum)

# # # using the f-String (modern way))
# # print("use the f-string")

# # name = "Bharat"
# # age = 23
# # print(f"my name is {name} and my age is {age} year old")

# # # float formatting
# # print(f"Float formatting ")
# # marks =23.2
# # print(f"your marks is {marks:}")


# # #Raw String 
# # print("raw\nString  ")
# # print("HI\nMY NAME IS BHARAT \n MY FATHER NAME \t IS NAGNATH KADAM ")
# # print("D:\Python\DataTypes.py")
# # #operator
# # print("Operator")
# # def create_user(name, email, **extra):
# #     print("Name:", name)
# #     print("Email:", email)
# #     print("Extra:", extra)

# # create_user(
# #     "Bharat",
# #     "bharat@gmail.com",
# #     city="Pune",
# #     age=21
# # )

# # functions to add two numbers 

# def add_two_numbers(a,b):
#     return a+b
# result=add_two_numbers(34,23)
# print(result)

# print(f"function to find square of number ")

# def square(number):
#     return number *number
# result = square(5)
# print(result)

# print("Function to Find Factorial")
# # using the loop 
# # import math
# # result =math.factorial(5)
# # print(result)

# print("Function to Find Factorial")

# # 1. Corrected function definition
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result  # Moved outside the for loop

# # 2. Corrected input and print logic
# # num = int(input("Enter a number to find its factorial: "))
# # print(f"The factorial of {num} is: {factorial(num)}")


# print("Function to Check Prime Number")

# def is_prime(n):
#     """Returns True if n is prime, False otherwise."""
#     # Numbers less than or equal to 1 are not prime
#     if n <= 1:
#         return False
    
#     # 2 is the only even prime number
#     if n == 2:
#         return True
    
#     # Exclude all other even numbers quickly
#     if n % 2 == 0:
#         return False
    
#     # Check odd factors up to the square root of n
#     # We step by 2 to skip even numbers (3, 5, 7, etc.)
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False  # Found a divisor, so it is not prime
            
#     return True  # No divisors found, it is prime

# # Get user input and test the function
# num = int(input("Enter a number to check: "))

# if is_prime(num):
#     print(f"{num} is a Prime Number.")
# else:
#     print(f"{num} is NOT a Prime Number.")

"""List Programs"""
#  print positive element 
# nums=[12,43,-33,54,12,24,-54,-7,5,-43,24,9]
# print("this is positive numbers:")
# for num in nums:

#     if num > 0:
#         print(num)
# print("this is negative numbers:")
# for num in nums:
#     if num < 0:
#         print(num)

#find the list sum of list 

# total=sum(nums)
# print("sum of the total numbers:",total)

# mean=total/len(nums)
# print("the average of this give list:",mean)

# largest=min(nums)
# index=nums.index(largest)
# print(largest)


# print("index:",index)

# greatest=max(nums)
# index=nums.index(greatest)
# print("greatest: ",greatest)
# print("index:",index)

# nums.sort()

# print("Second Greatest:", nums[-2])

# print("List of duplications ")
# unique=list(set(nums))
# print(unique)

# unique=[]
# for num in nums:
#     if num not in unique:
#         unique.append(num)
# print(unique)    

"""Python quick revision notes """
#variables is named memory location used to store data
#name variable 
name="bharat" #name is variable and bharat is values
#2 data types int float str bool list tuple set dict

# 3 types conversion
#implicit 
a=10
b=22.2
d=a+b
print(d)
print(type(d))

print(f"explicit")
x="10"
# print(x)
print(type(x))
print(int(x))
# print(type(x))

# print("input and output")
# name=input("enter name")
# print(name)
# age=int(input("enter age"))
# print(age)

print("indexing")
name="Python"
print(name[0])
print(name[-1])
print("slicing")
print(name[1:4])
print("reverse string")
print(name[::-1])

print("odr() and chr()")
print(ord('A'))
print(chr(56))

#operators arithmetic comparison logical conditional statements 
print("conditional statements")

# age=int(input("enter your age:"))
# if age >=18:
#     print("adult")
# else:
#     print("minor")
    

print("elif")  

# marks=float(input("enter your marks"))
# if marks >= 90:
#     print("A")
# elif marks >= 70:
#     print("B")
# elif marks >= 50:
#     print("C")
# else:
#     print("fail")

# print("loop")
# #for loop
# for i in range(1,6):
#     print(i)

# #while loop
# i=0
# while i<=10:
#     print(i*5)
#     i +=1

# print("functions \n ")
# # a function is a reusable block of code 

# def greet():
#     print("hello")
# greet()

# #parameters and arguments

# # def add(a,b):
# #     return a+b
# # sum=add(23,23)
# # print(sum)
# # print(add(32,32))

# #types of arguments
# # 1 positional
# # def add(a,b):
# #    print(a+b)
# # add(a=10,b=40)


# print("list \n")
# # a list is an ordered mutable collection that allows duplicate elements and heterogeneous data

# #syntax
# list=[12,12,23,34,56,-5,"Bharat",45.3]
# print(list)
# print(list[5])
# # print(list[5]=34)
# # list[5]=2
# # print(list)
# #important methods

# list.append(400)
# list.append([300,900])
# print(list)

# list.insert(5,-5)

# list.remove(400)

# print(list)

# list.pop()
# print(list)
# print(list.count("Bharat"))
# print(list.index("Bharat"))
# print("sort elements")
# list.sort()
# print(list)

# tuple
print("tuple")
