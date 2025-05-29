# Count the number of digits in a number.

def count_digit(n):
    if n == 0:
        return 0 
    return count_digit(n // 10) + 1

print(count_digit(1234))