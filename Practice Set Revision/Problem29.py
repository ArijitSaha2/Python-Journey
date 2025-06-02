# Write a Python program to print "Hello, World!" five times using a loop.

n = 5

for i in range(1, n+1):
    print("Hello")

# Create a program that takes two numbers as input and prints their sum, difference, product, and quotient.

n1 = int(input('Enter Number1: '))
n2 = int(input('Enter Number2: '))

print(f'Sum = {n1 + n2}')
print(f'Difference = {n1 - n2}')
print(f'Product = {n1*n2}')
print(f'Quotient = {n1//n2}')