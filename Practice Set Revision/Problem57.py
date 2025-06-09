# Write a function that checks if a number is even.

def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(is_even(8))