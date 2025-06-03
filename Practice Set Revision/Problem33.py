# Write a recursive function to calculate the factorial of a number.

# Example:
# If input is 5, output should be 120 because 5 × 4 × 3 × 2 × 1 = 120.

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(5))