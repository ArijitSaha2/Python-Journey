# What's the key difference between lists and tuples in Python?

'''The key difference between lists and tuples in Python is that lists are mutable — we can change, add, or remove elements. Tuples are immutable — once created, their elements cannot be modified directly.'''

# Predict the output and explain:
a = [1, 2, 3]
a[0] = 100
print(a)
'''Output = a = [100,2,3] because lists are mutable and there values can be updated at any point.'''

# Predict the output and explain:
b = (1, 2, 3)
# b[0] = 100
# print(b)
'''Output will be an error as tuples aren't mutable and there values cannot be updated directly.'''

# 4. Write a program that:
"""Takes 5 numbers as input (from the user)
Stores them in a list
Prints the list"""

l= []

for i in range(1, 6):
    num = int(input(f"Enter your number {i}: "))
    l.append(num)
print(l)