def print_range_1_10():
    for i in range(1,10):
        print(i)
        
        
def print_range_10_1():
    for i in range(10,0,-1):
        print(i)



def even_odd(num):
    if(num%2==0):
        print('this is the even number:',num)
    else:
        print('this is the odd number:',num)
            

def print_table(numbers=5):
    for i in range(1,11):
        print(i*numbers)
        
        
def sum_natural_number(num):
    total=(num * (num+1)) // 2
    print(total)
    
    
    
# using the for loop  

def sum_using_for_loop(n):
    total_sum = 0
    for i in range(1, n+1):
        # total_sum += i  
        total_sum=total_sum + i
    print('total sum of natural numbers using the for loop:',total_sum)

import math 


def factorial1(num):
    result=math.factorial(num)
    # print(result)
    print('factorial:',result)
    
    
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return print('result is using the loop:',result)




# print(factorial_loop(5))  
