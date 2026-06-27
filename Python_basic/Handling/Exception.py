"""Exceptions Handling"""
#
# a=int(input("enter any number:"))
# try:
#     total=10/a
# except Exception as err:
#     print(f"sorry there is an err as {err}")
# else:
#     print("good there is no exceptions ")
# finally:
#     print("i will run no matter what")

# print("ok i have done the division")


# age =int(input("tell your age:"))
# try:
#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")
# except Exception as err:
#     print(f"an error occured as {err}")
# print("the club will start soon")

#syntax error
#atm withdrawal 
balance =int(input("enter your balance:"))
try:
    amount=int(input("enter withdrawal amount:"))
    if amount > balance:
        raise ValueError("insufficient Balance")
except ValueError as err:
    print("error:",err)
else:
    balance -=amount
    print("withdrawal successful")
    print("remaining balance :",balance)
finally:
    print("thank you for using atm")
