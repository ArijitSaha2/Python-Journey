# count digits in n recursively.

def count_digits(n):
    if n == 0:
        return 0
    return count_digits(n // 10) + 1

print(count_digits(12345))