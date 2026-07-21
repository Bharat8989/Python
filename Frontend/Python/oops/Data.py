data=[
    10,20,30,2,43,2,4,234,7
]

print(data)

# adding elements 
data.append(90)
print(data)
data.insert(2,80)
print(data)
data.extend((100,200,300))
print(data)


# removing elements ()

print('removing elements ')


data.remove(7)
print(data)

#  pop is the removes indexing the positions 

data.pop(0)
print(data)


# data.clear()
# print(data)

del data[2]
print(data)

print('accessing and searching ')

print(data[2])
print(data.index(90))
print(data.count(2))
print(90 in data)


print("modifying and organizing")

data[2]=1000
print(data)
data.sort()
print(data)


data.reverse()
print(data)

print("list ")

print(len(data))
print(max(data))
print(min(data))
print(sum(data))