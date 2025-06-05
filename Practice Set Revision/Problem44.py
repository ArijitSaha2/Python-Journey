# Write a function that checks whether a number is even or odd.

def is_even(n):
    if n % 2 == 0:
        return f"{n} is Even"
    else:
        return f"{n} is Odd"

n = int(input('Enter Number: '))    
print(is_even(n))