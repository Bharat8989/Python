from math_functions import (
    add_binary,  sub_binary, mul_binary,div_binary, hex_to_dec, 
    dec_to_hex,add_normal,sub_normal,mul_normal,div_normal
)

def run_calculator():
    print("--- Multi-Calculator ---")
    print("1. Normal Calculator (+, -, *, /)")
    print("2. Binary Operations (+, -, *, /)")
    print("3. Hexadecimal Converter")
    choice = input("Select an option (1, 2, or 3): ")
    # normal 
    if choice =='1':
        n1=float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        n2 = float(input("Enter second number: "))
        
        if op == '+':
            print(f"Result:{add_normal(n1,n2)}")
        elif op == '-':
            print(f"Result: {sub_normal(n1, n2)}")
        elif op == '*':
            print(f"Result: {mul_normal(n1, n2)}")
        elif op == '/':
            print(f"Result: {div_normal(n1, n2)}")
        else:
            print("Invalid operator!")
            
            
            
    elif choice == '2':
        bin1 = input("Enter first binary number: ")
        op = input("Enter operator (+, -, *, /): ")
        bin2 = input("Enter second binary number: ")
        
        if op == '+':
            print(f"Result: {add_binary(bin1, bin2)}")
        elif op == '-':
            print(f"Result: {sub_binary(bin1, bin2)}")
        elif op == '*':
            print(f"Result: {mul_binary(bin1, bin2)}")
        elif op == '/':
            print(f"Result: {div_binary(bin1, bin2)}")
        else:
            print("Invalid operator!")
            
            
    elif choice == '3':
        print("A hex to decimal")
        print("B decimal to hex")
        sub_choice = input("Select an option (A or B): ")
        if sub_choice.upper() == 'A': 
            h=input("Enter hexadecimal number: ")
            print(f"Decimal: {hex_to_dec(h)}")  
        elif sub_binary=='B':
            d=input("Enter decimal number: ")
            print(f"Hexadecimal: {dec_to_hex(d)}")
        else:
            print('Invalid choice ')

run_calculator()