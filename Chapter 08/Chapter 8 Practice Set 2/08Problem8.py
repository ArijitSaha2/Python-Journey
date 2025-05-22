# Write a function sum_three(a, b, c) that takes 3 arguments and returns their sum.
# Then, call it using variables as arguments and print the result.

def sum_three(a, b, c):
    return a + b + c

d = int(input('Enter your Number: '))
e = int(input('Enter your Number: '))
f = int(input('Enter your Number: '))

result = sum_three(d, e, f)
print(f"The sum is: {result}")