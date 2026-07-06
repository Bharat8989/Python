# name='bharat'
# age=23
# floatt =34.2
# value=True
# lst=[1,2,3]
# tup=(1,2,3,4,5)
# seta={12,'bharat',34.32}
# dicts={'age':23,'id':101,'score':49,'name':'bharat'}

# print(type(name))
# print(type(age))
# print(type(floatt))
# print(type(lst))
# print(type(tup))
# print(type(seta))
# print(type(dicts))
# print(dicts)


# types of conversion 
# implicit 
# a=10
# b=12.2
# print(a+b)
# print(type(a+b))
# print(int(a+b))
# c=12
# d=34
# print(type(str(c+d)))
# print(type(c+d))

# input and output system 

# name=input(('enter your name:'))
# age=int(input('enter your age:'))
# num1=int(input('enter your first numbers:'))
# num2=float(input('enter your second numbers:'))

# total =num1+num2
# print("total additions of two numbers:",total)


# indexing 
# name='suraj'
# name='pavan'  #value overwriting or variable reassignment

# print(name[2])

# # slicing
# print(name[1:4])
# print(name[:])
# print(name[1::1])

# # ord() and chr()

# print(ord('A'))
# print(chr(34))



# # operators 
# print('arithmetic operators ')
# a=19
# b=7
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a/b)
# print(a//b)
# print(b**b)


# comparison
# print('comparison')
# print('aa'=='bb') #false
# print('aa'!='bb')   #True
# print(a>=b)   #false
# print(b>=a)   #true


# print('logical operations')
# age=18
# weight=50
# print(a >=age and 51 >= weight) #true

# print(a >= age and 45 >=weight) #false

# print(12 >= age and 88 >=weight) #false
# print(2 >= age and 4 >=weight)   #false


# print('conditional statements ')


"""Conditional statements problems """

# positive ,negative or zero
# num=int(input('enter any  numbers:'))

# if num > 0:
#     print('positive numbers')
# elif num < 0:
#     print('negative numbers')
# else:
#     print('zero')

# problem 2 even or odd numbers 

# if num % 2 ==0:
#     print('even numbers')
# else:
#     print('odd numbers')

# problem voting eligibility numbers

# age = int(input('enter your age :'))
# if age >=18 :
#     print("eligible ")

# else:
#     print('not eligible ')

# problem 4 largest of two numbers 

# num1=int(input('enter num1:'))
# num2=int(input('enter num2:'))
# num3 =int(input('enter num3:'))
# if num1 >= num2 and num1 >=num3 :
#     print(f'{num1} is grater')

# elif num2 >=num1 and num2 >=num3:
#     print(f'{num2} is grater numbers')

# else:
#     print(f'{num3} is greater numbers')

# if num1 > num2:
#     print('num 1 is grater numbers')
# else:
#     print('num2 is greater number')


# year=int(input('enter year:'))
# if (year % 400==0) or (year % 4 ==0 and year % 100 !=0):
#     print('leap year')
# else:
#     print('not leap year')



# loops in python 
# print('for loop')

# # even numbers 

# for i in range(2,20,2):
#     print(i)
    
# # reverse counting
# print('reverse counting')
# for i in range(10,0,-1):
#     print(i,end=' ')
    
# print('iterating through string ')

# name ='python'
# for ch in name:
#     print(ch)
    
# fruits=['apple','mango','banana']
# for fruit in fruits:
#     print(fruit)
    
#     # while loop
    
# print('while loop')

# i=1
# while i<=5:
#     print(i)
#     i +=1

# print('countdown')
# i=10
# while i>=1:
#     print(i)
#     i -=1
    
    
# print('user password')

# # while True:
# #     password=input('enter your password:')
# #     if password =='bharat':
# #         print('login successful')
# #         break 
# #     elif password=='':
# #         print('password cannot be empty .try again.')
# #     else:
# #         print('incorrect password access denied. try again.\n')


# print('break statement')

# for i in range(1,11):
#     if i==3:
#         # break
#         continue
#     print(i)
    
    
# print('nested loop')
# for i in range(3):
#     for j in range(3):
#         print(i, j)

# print('sum of 1 to 100')

# total=0
# for i in range(1,101):
#     total =total+i
# print('total',total)


print('print all even numbers 1 to 100')

for i in range(2,101,2):
    print(i)

print('odd numbers')
for i in range (1 ,101,2):
    print(i)
    
print('square of numbers')
for i in range(1,21):
    print(i ** 2)