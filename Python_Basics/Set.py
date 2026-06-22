"""Set in Python"""
# a set is an unordered mutable collection of unique element 
#properties of set 1 unordered (set does not maintain insertion order.)
s={10,20,1,40,50}
print(s)
s.add(45)
print(s)

# not duplications (duplication values are automatically removed )
p={10,10,20,30,40, 40,50}
print("no duplication :")
print(p)
# print(p)  
print("pop output") 
print(s.pop())

#set operations 
print("union")
a={1,2,3,4}
b={3,4,5,6}
print(a | b)
print("intersection")
print(a & b)
print("difference")
print(a-b)

print("symmetric difference")
print(a ^ b)
nums=[10,20,10,30,20]
unique= list(set(nums))
print(unique)

