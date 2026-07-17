# def counting_numbers():
#     numbers=1220.41

#     name='python'

#     print(len(str(numbers)))
#     print(len(name))
    
# # def counting_char(name):
# #     for i in range(0,name+1):
# #         print(i)
        
# # counting_char('python')

# def square_numbers(n):
#     print('the square number using the loop')
#     for i in range(1,n+1):
#         print(i ** 2)

# from decorators import about

# about()
    
# class Node:
#     def __init__(self, data):
#         self.data = data  # Holds the actual value
#         self.next = None  # Points to the next node (initially None)
#         self.prev = None  # Points to the previous node (initially None)


# # 1. Create three separate nodes
# node1 = Node("Apple")
# node2 = Node("Banana")
# node3 = Node("Cherry")

# # 2. Link Node 1 and Node 2
# node1.next = node2
# node2.prev = node1

# # 3. Link Node 2 and Node 3
# node2.next = node3
# node3.prev = node2

# # Start at the middle node (Banana)
# current = node2

# print(current.data)       # Output: Banana
# print(current.next.data)  # Output: Cherry  (Moves forward)
# print(current.prev.data)  # Output: Apple   (Moves backward)


# try: 
#     num = int(input("Enter Number: ")) 
# except ValueError: 
#     print("Invalid Input") 
# else: 
#     print("You entered:", num) 


# exception handling in python 

# try -> contains risky code 
# except handle errors 
# else executes if no error occurs 
#  finally executes whether error occurs or not 
#  raise -> create custom exception 



#  try and except 

# try: 
#     num1=int(input('enter the num1:'))
#     num2=int(input('enter the num 2:'))
#     division =num1/num2

#     print('division:',division)

# except Exception as err:
#     print('please enter number only')
#     print('this is error for ',err)
#     print(type(err))

# finally:
#     print("execute whether error occurs or not ")


# try:
#     age=int(input('enter the your age'))
#     if age>=18:
#         print('adult')

#     else:
#         print('not adult')
# except Exception as err:
#     print('enter Integer number only ')
#     print(type(err))
    
# else:
#     print('you entered:',age)

#  file handling there are two types 1 text file and 2 binary files 

file =open('notes.txt','r')

print(file.read())
file.close()

file =open('notes.txt','w')
file.write('python html')
# file.close()


# append mode (a)

file =open('notes.txt','a')
file.write('\njava')
file.close()


file=open('new.txt','x')
file.write('javascript')
# print(file.read())
file.close()


import os 

if os.path.exists('new.txt'):
    os.remove('new.txt')
else:
    print('file not found')


import os

print(os.path.abspath("notes.txt"))