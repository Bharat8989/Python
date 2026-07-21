# check existence 

data=[1,23,4,5,36,7,76,48,8765,90]

# check if exists 

print(980 in data)

# indexing position

print(data.index(7))

# count how many time 
print(data.count(23))



# filtering a list 

# keep only numbers greater than 200

filtered_list =[x for x in data if x < 70]

print(filtered_list)



# sorting a list 

data.sort()
print(data)


data.sort(reverse=True)
print(data)

# mapping a list 



# iterable

my_list=[10,20,30]

extra_items=[40,50,60]
my_list.extend(extra_items)
print(my_list)



