# set1={12,12,23,43,345,543,23,543,'python','html',23.2}
# # element do not maintain insertion order.
# # unique elements

# print(set1)

# set1.add(59)
# print(set1)

# set1.remove('python')
# print(set1)

# arr={23,123}
# print(type(arr))

# arr1={"name":'bharat'}
# print(type(arr1))


# def fun(limit):
#     for i in range (2,limit+1,2):
#         print(i)
#         return i
        

# obj=fun(12)

# print(obj)


def fun(limit):
    for i in range (2,limit+1,2):
        print(f'print {i}')
        yield i
        
obj=fun(12)
print(next(obj))
print(next(obj))