# Write a function that counts how many digits are in a given positive integer.

def count_digits(n):
    if n == 0:
        return 0
    return count_digits(n // 10) + 1

print(count_digits(1234))