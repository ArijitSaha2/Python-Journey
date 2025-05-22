# Write a function greet_all(names) that takes a list of names as a parameter and prints a greeting for each name.
'''Example: greet_all(["Alice", "Bob", "Charlie"])'''

def greet_all(names):
    for name in names:
        print(f"Welcome {name}!")

lst = ["Alice", "Bob", "Charlie"]
greet_all(lst)
