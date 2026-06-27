# print positive and negative elements 

nums=[1,2,45,63,-2,-34,-1,-23.2]
print("all numbers for the orders")

nums.sort()
print(nums)
print("positive numbers:-")
for num in nums:
   if num >0:
    print(num)

print("negative Numbers:")
for num in nums:
  if num < 0:
    print(num)

print("average of the list elements ")
total=sum(nums)
print("total=",total)
mean=total/ len(nums)
print(len(nums))
print("mean=",mean)

print("greatest element and its index")
def greatest_element(lst):
    greatest = max(lst)
    index = lst.index(greatest)

    print("Greatest =", greatest)
    print("Index =", index)

nums = [10, 55, 20, 80, 40]

greatest_element(nums)
