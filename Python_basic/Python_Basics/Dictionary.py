"""Dictionaries in Python """
# a dictionary is a collection of key value pairs 
print("create a dictionary")
student={1:10,2:20,3:30,4:40,5:40,"name":"bharat"}
print(student)
# print(student[0])
#accessing the values 
print(student["name"])
print(student[1])
print("using the get ")
print(student.get(2))

print("updating values ")
student[3]=300
print(student)
print("adding the new key value pair")
student[5]=500
print(student)

print("removing the items")
print("using the pop()")
student.pop(5)
print(student)

print ("dictionary traversing ")
#traverse keys 
for key in student:
    print(key)

print("traverse values")
for value in student.values():
    print(value)

print("traverse key value pairs")
for key, value in student.items():
    print(key , value)

print("important dictionary method ")
print(student.keys())
print(student.values())
print(student.items())
print("duplicate keys")

#the last values overwrite the previous one 
import copy
print("shallow copy and deep copy ")
d1 ={
    "name":"Bharat",
    "marks":[90,80]
}
d2=copy.copy(d1)
d2["marks"].append(70)
print(d1)
print(d2)

#merge two dictionaries
d1={"a":10,"b":20}
d2={"c":30,"d":40}
d1.update(d2)
print(d1)

#sum all values in a dictionary
total=sum (d1.values())
print("sum=",total)

#count frequency of each elements

nums =[10,20,30,40,50,10]
freq={}
for num in nums:
    if num in freq:
        freq[num] +=1
    else:
        freq[num]=1

print(freq)

#frequency of characters in a sting

text = "python"

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq) 