# variable is a named memory location used to store data 

name='bharat'
age=23
floatt =34.2
value=True
lst=[1,2,3]
tup=(1,2,3,4,5)
seta={12,'bharat',34.32}
dicts={'age':23,'id':101,'score':49,'name':'bharat'}

print(type(name))
print(type(age))
print(type(floatt))
print(type(lst))
print(type(tup))
print(type(seta))
print(type(dicts))
print(dicts)


# types of conversion 
# implicit 
a=10
b=12.2
print(a+b)
print(type(a+b))
print(int(a+b))
c=12
d=34
print(type(str(c+d)))
print(type(c+d))

# input and output system 

# name=input(('enter your name:'))
# age=int(input('enter your age:'))
# num1=int(input('enter your first numbers:'))
# num2=float(input('enter your second numbers:'))

# total =num1+num2
# print("total additions of two numbers:",total)


# indexing 
name='suraj'
name='pavan'  #value overwriting or variable reassignment

print(name[2])

# slicing
print(name[1:4])
print(name[:])
print(name[1::1])

# ord() and chr()

print(ord('A'))
print(chr(34))



# operators 
print('arithmetic operators ')
a=19
b=7
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a//b)
print(b**b)


# comparison
print('comparison')
print('aa'=='bb') #false
print('aa'!='bb')   #True
print(a>=b)   #false
print(b>=a)   #true


print('logical operations')
age=18
weight=50
print(a >=age and 51 >= weight) #true

print(a >= age and 45 >=weight) #false

print(12 >= age and 88 >=weight) #false
print(2 >= age and 4 >=weight)   #false


print('conditional statements ')



