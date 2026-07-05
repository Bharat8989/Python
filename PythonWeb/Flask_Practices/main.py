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

name=input(('enter your name:'))
age=int(input('enter your age:'))
num1=int(input('enter your first numbers:'))
num2=float(input('enter your second numbers:'))

total =num1+num2
print("total additions of two numbers:",total)


