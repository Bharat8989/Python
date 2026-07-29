print("--- Polymorphism with 4 Number System Calculators ---")

# Parent Class
class BaseCalculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

# 1. Decimal Calculator (Standard Numbers: 10, 20, etc.)
class DecimalCalculator(BaseCalculator):
    pass 

# 2. Binary Calculator (Base 2: Output will look like 0b1010)
class BinaryCalculator(BaseCalculator):
    def add(self, a, b):
        # super().add(a, b) calls the parent math, then bin() converts it to binary
        return bin(super().add(a, b))

    def sub(self, a, b):
        return bin(super().sub(a, b))

    def multiplication(self, a, b):
        return bin(super().multiplication(a, b))

# 3. HexCalculator (Base 16: Output will look like 0x1a)
class HexCalculator(BaseCalculator):
    def add(self, a, b):
        return hex(super().add(a, b))

    def sub(self, a, b):
        return hex(super().sub(a, b))

    def multiplication(self, a, b):
        return hex(super().multiplication(a, b))

# 4. OctaCalculator (Base 8: Output will look like 0o12)
class OctaCalculator(BaseCalculator):
    def add(self, a, b):
        return oct(super().add(a, b))

    def sub(self, a, b):
        return oct(super().sub(a, b))

    def multiplication(self, a, b):
        return oct(super().multiplication(a, b))


# --- HOW TO USE IT (Testing Polymorphism) ---

# We take two normal numbers for testing
num1 = 12
num2 = 4

# Create a list of all 4 calculator objects
calculators = [
    DecimalCalculator(),
    BinaryCalculator(),
    HexCalculator(),
    OctaCalculator()
]

# A single loop triggers the same functions, but gives different outputs!
for calc in calculators:
    # __class__.__name__ just prints the name of the class dynamically
    print(f"\nResults using {calc.__class__.__name__}:")
    print(f"Addition (12 + 4)       = {calc.add(num1, num2)}")
    print(f"Subtraction (12 - 4)    = {calc.sub(num1, num2)}")
    print(f"Multiplication (12 * 4) = {calc.multiplication(num1, num2)}")
