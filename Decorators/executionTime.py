"""Decorator """
# def decorator(func):
#     def wrapper():
#         print("before functions ")

#         func()
#         print("after functions ")
#     return wrapper
# @decorator
# def hello():
#     print("hello")
# hello()

from functools import wraps
is_logged_in = True

def check_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("please login first ")
    return wrapper  #

@check_login
def view_profile():
    print("your profile data is :Bharat Kadam , Pune ")

@check_login
def transfer_money(amount):
    print(f"${amount}")


print("profile trying ")
view_profile()

print("\nmony trasfer trying")
transfer_money(5000)
