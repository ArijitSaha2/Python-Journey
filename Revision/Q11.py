# What are f-strings in Python? Give an example.

"""
f-strings are used when we need to type multiple values with variables.
E.g. print(f"Welcome, {name}")"""

# Predict the output and explain:

a = "hello"
print(a[:4]) # Or print(a[0:4]) same thing
"""
It will print 'ell' as the starting point of variable a is 1, else it would have printed hell if it started from 0"""

# Write a program that:
'''
Takes a user's name
Prints a welcome message using f-string
Example: "Welcome, Ankit!" '''

name = input("Enter your name: ")

print(f"Welcome, {name}")