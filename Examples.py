# """Sum of two Numbers"""
# #using the user input 

# # num1=int(input("enter the first number:"))
# # num2=int(input("enter the second number :"))
# # # num1=int(num1)
# # sum =num1+num2
# # #the valule of the give num1 and num2

# # print("the num1 values is :",num1, "and num2 value is :",num2)

# # print("the sum of the num1 and num2 is :",sum)

# # using the f-String (modern way))
# print("use the f-string")

# name = "Bharat"
# age = 23
# print(f"my name is {name} and my age is {age} year old")

# # float formatting
# print(f"Float formatting ")
# marks =23.2
# print(f"your marks is {marks:}")


# #Raw String 
# print("raw\nString  ")
# print("HI\nMY NAME IS BHARAT \n MY FATHER NAME \t IS NAGNATH KADAM ")
# print("D:\Python\DataTypes.py")
# #operator
# print("Operator")
# def create_user(name, email, **extra):
#     print("Name:", name)
#     print("Email:", email)
#     print("Extra:", extra)

# create_user(
#     "Bharat",
#     "bharat@gmail.com",
#     city="Pune",
#     age=21
# )

# functions to add two numbers 

def add_two_numbers(a,b):
    return a+b
result=add_two_numbers(34,23)
print(result)

print(f"function to find square of number ")

def square(number):
    return number *number
result = square(5)
print(result)

print("Function to Find Factorial")
# using the loop 
# import math
# result =math.factorial(5)
# print(result)

print("Function to Find Factorial")

# 1. Corrected function definition
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result  # Moved outside the for loop

# 2. Corrected input and print logic
# num = int(input("Enter a number to find its factorial: "))
# print(f"The factorial of {num} is: {factorial(num)}")


print("Function to Check Prime Number")

def is_prime(n):
    """Returns True if n is prime, False otherwise."""
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # Exclude all other even numbers quickly
    if n % 2 == 0:
        return False
    
    # Check odd factors up to the square root of n
    # We step by 2 to skip even numbers (3, 5, 7, etc.)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False  # Found a divisor, so it is not prime
            
    return True  # No divisors found, it is prime

# Get user input and test the function
num = int(input("Enter a number to check: "))

if is_prime(num):
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is NOT a Prime Number.")
