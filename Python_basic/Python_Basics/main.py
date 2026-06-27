#value bits and bytes 
a=65
print(bin(a))
print(oct(a))

print(ord('A'))
print(chr(a))
b=49
print(chr(b))
import sys
print(sys.getsizeof(a))
name = "Bharat"
print(sys.getsizeof(name))
print(name[5])
fruits=["apple", "banana", "mango"]
print(fruits[2])

#stirng slicing 
Name="SurajKrushnaKadam"
print(Name[1::2])
print(Name[0:])


print("conversion of data types ")
#integer to stirng
age =23
print(type(age))

age=str(age)
print(type(age))

#string to integer 
integer_age="23"
print(type(integer_age))
integer_age=int(integer_age)
print(type(integer_age))

#types of coversion 
""" implicit type and explicit types 
    implicit automatic data type change karte

   
   """
k=20
j=20.3
c=j+k
print(c)
print(type(c))