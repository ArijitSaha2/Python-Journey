# Write a recursive function to calculate the sum of digits of a number.
# Example: sum_digits(1234) → 1 + 2 + 3 + 4 = 10

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))