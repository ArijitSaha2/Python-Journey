# Write a function add(a, b) that takes two numbers and returns their sum.

def  add(a, b):
    return (f"{a} + {b} = {a+b}")

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))

print(add(a, b))