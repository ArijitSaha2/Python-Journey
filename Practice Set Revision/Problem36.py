# Write a function that takes a number and returns whether it is positive, negative, or zero.

def check(n):
    if n < 0:
        return f"{n} is Negative"
    elif n > 0:
        return f"{n} is Positive"
    else:
        return "It is Zero"

n = int(input('Enter Number: '))
print(check(n))