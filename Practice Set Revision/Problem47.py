# Write a function that returns the sum of the digits of a number.

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10) 

print(sum_digits(1234))