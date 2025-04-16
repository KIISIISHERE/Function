#Define the Functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
# Ask user for choice
print("Choose Operation: +, -, *, /")
op = input("Enter Operator: ")
#Ask For Numbers
a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))
# Perform Operation
if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", subtract(a, b))
elif op == "*":
    print("Result:", multiply(a, b)) 
elif op == "/":
    if b !=0:
        print("Result:", divide(a, b)) 
    else:
        print("Cannot Divide By Zero (0).")
else: print("Invalid Operator.")
