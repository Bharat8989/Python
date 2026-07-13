# def login_required(func):
#     def wrapper(name,age):
#         print("Checking Login...")
#         func(name, age)
#     return wrapper


# @login_required
# def profile(name, age):
#     print("Welcome User", "name:", name,  "Age:", age)


# profile("Bharat", 22)



def check_role(required_role):
    def decorator(func):
        def wrapper(user_role):
            if user_role== required_role:
                return func(user_role)
            else:
                print("Access Denied! You do not have the required role.")
        
        return wrapper
    return decorator

@check_role(required_role="admin")

def delete_database(user_role):
    print("Database deleted successfully!")
    
delete_database("admin")  # Output: Database deleted successfully!
# delete_database("user")   # Output: Access Denied! You do not have the required