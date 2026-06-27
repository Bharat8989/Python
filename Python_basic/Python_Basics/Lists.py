""" Data Structure
     In-build data structure 
     1 List 2 Tuple 3 Dictionary 4 Set

     custom data structure 
     stack queue ,linked list ,graph etc

 """
# List Powers 


# list manje anek values ekach varible madhye store karnyasathi vaprle janare data structure 
fruits =["apple", "mango","banana"]

# 1 ordered list element 
print(fruits)
print(fruits[1])
print(fruits[0:2])
print(fruits[0:3])
print(fruits[0::2])
print(fruits[0])

print("mutable")

fruits[1]="Orange"
print(fruits)

print("3 Duplicates Allowed ")

numbers =[12,22,12,12,32,22]
print(numbers)

print("4 heterogeneous")

data=["bharat",12,12.2,True,False]
print(data)
print("append()")
data.append("color")
print(data)

print("insert()")
data.insert(2,"hi ")
print(data)

print("extend()")
a=[1,2]
b=[3,4]
a.extend(b)
print(a)

a.remove(1)
print(a)
a.pop(2)
print(a)

a.clear()
print(a)

numbers=[3,4,2,1,67,12,89,23]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

print(len(numbers))

print("using the index")
for i in range(len(numbers)):
    print(i, numbers[i])

print("directly on values")
for number in numbers:
    print(number) 

print(dir(list))
help(list)



# print(data[-1])

# print("List traversing")
# for fruit in fruits:
#     print(fruit)

# for i in range(len(fruits)):
#     print(fruits[i])

# important list method 


