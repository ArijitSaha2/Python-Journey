# Write a function is_even(num) that returns True if num is even, otherwise False.

def is_even(num):
    return num % 2 == 0
    
num = int(input("Enter your number: "))
print(is_even(num))
