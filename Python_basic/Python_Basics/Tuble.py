"""tuple is an ordered collection of elements that is immutable allow duplicates and can store heterogeneous data"""

# 1 immutable (once a tuple is create its element cannot be changes)
t=(123,12,3,43,34,12,12)
print(t)
print(t[0])
# t[2]=10
# print(t)

# ordered (elements maintain their insertion order )
# tuple can store different data types 
student=("bharat",23, 8.223,True)
print(student)

print(t.count(12)) 