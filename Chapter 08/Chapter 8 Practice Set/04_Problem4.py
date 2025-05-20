# write a recursive function to calculate the sum of first n natural numbers.

def sumf(n):
    if n == 1:
        return 1
    return n + sumf(n-1)

n = int(input("Enter your number: "))
print(f'Sum is {sumf(n)}')