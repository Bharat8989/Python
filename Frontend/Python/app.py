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
    
class Node:
    def __init__(self, data):
        self.data = data  # Holds the actual value
        self.next = None  # Points to the next node (initially None)
        self.prev = None  # Points to the previous node (initially None)


# 1. Create three separate nodes
node1 = Node("Apple")
node2 = Node("Banana")
node3 = Node("Cherry")

# 2. Link Node 1 and Node 2
node1.next = node2
node2.prev = node1

# 3. Link Node 2 and Node 3
node2.next = node3
node3.prev = node2

# Start at the middle node (Banana)
current = node2

print(current.data)       # Output: Banana
print(current.next.data)  # Output: Cherry  (Moves forward)
print(current.prev.data)  # Output: Apple   (Moves backward)










