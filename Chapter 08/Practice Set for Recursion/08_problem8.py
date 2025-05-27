# Write a recursive function to find the factorial of a number.
# Example: factorial(5) → 5 x 4 x 3 x 2 x 1 = 120

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))