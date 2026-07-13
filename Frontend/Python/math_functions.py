# --- Binary Operations ---
def add_binary(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

def sub_binary(bin1, bin2):
    return bin(int(bin1, 2) - int(bin2, 2))[2:]

def mul_binary(bin1, bin2):
    return bin(int(bin1, 2) * int(bin2, 2))[2:]

def div_binary(bin1, bin2):
    return bin(int(bin1, 2) // int(bin2, 2))[2:]

# --- Conversions ---
def hex_to_dec(hex_str):
    return int(hex_str, 16)

def dec_to_hex(dec_num):
    return hex(int(dec_num))[2:].upper()

# --- Normal Decimal Operations ---
def add_normal(num1, num2):
    return num1 + num2

def sub_normal(num1, num2):
    return num1 - num2

def mul_normal(num1, num2):
    return num1 * num2

def div_normal(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2
