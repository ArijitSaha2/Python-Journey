# What’s the difference between mutable and immutable datatypes in Python?

''' 
Immutable datatypes can't have their existing values changed (e.g., int, str, tuple). We can assign new values but can't modify the old one.
Mutable datatypes like list, dict, or set let you change, remove, or add elements.'''

# Predict the output and explain:
a = "5"
b = 3
print(a * b)
'''
It will print "5" * 3 → '555'
As a is a string and b is an integer, when we write print(a * b) in python the string is multiplied 3 times by "5" meaning it will print a string 3 times.'''

# What will this print and why?
x = None
print(type(x))
'''
None is a special constant that represents "no value".
The type of None is NoneType, which is a built-in Python type.'''

# Write code to:
'''
Store your name, age, and whether you're a student in
variables.
Print all of them with their data types using type()'''

name = input("Enter your Name: ")
age = int(input("Enter your age: "))
student = True
print(type(name))
print(type(age))
print(type(student))