""" Conditional statement in Python  """
#if statement 
#using the user input for the give conditional statement 
#if else and elif

# accept two numbers and print the greatest between them 
# accept an integer and check whether it is an even number or odd 

year=int(input("enter any year :-"))
# if number%2==0:
#     print("even number ")
# else:
#     print("old number ")
#leap year
if year%400==0:
    print("lear year")
elif year % 100==0:
    print("not leap year")
elif year%4==0:
    print("lear year")
else:
    print("not lear year")
