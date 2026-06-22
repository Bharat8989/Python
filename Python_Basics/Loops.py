"""Loops in python 
   there are two type of loops 1 for loop and 2 while loop 

"""
# repetitions chi number mahit aashot tevha for loop use karatat
"""for loop syntax 
for variable in range(start , stop , step)
     statement
"""
# for i in range(1,6):
#     print(i)

# num =5
# for i in range(1,11):
#     print(num*i)

# while condition :
   #statement 
# i=1

# while i<=5:
#     print(i)
#     i +=1

#ATM PIN
# secret = 7

# while True:
#     guess = int(input("Guess the Number: "))

#     if guess == secret:
#         print("🎉 You Won!")
#         break
#     else:
#         print("Try Again")


# orders = ["Order1", "Order2", "Order3"]

# for order in orders:
#     print(f"Processing {order}")

# practice Programs
# print 1 to 100 numbers 

# for i in range (1 ,101,1):
#     print(i)

# sum of first 100 numbers

# num=1
# while num<=100:
#     print(num)
#     num +=1

# total=0
# for i in range(1,101):
#     total +=i
   
# print(f"Sum ={total}")

# total =0
# i=1
# while i<=100:
#     total +=i
#     i +=1
# print(f"Sum={total}")
balance = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = int(input("Enter Deposit Amount: "))
        balance += amount
        print("Amount Deposited")

    elif choice == 3:
        amount = int(input("Enter Withdraw Amount: "))

        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")