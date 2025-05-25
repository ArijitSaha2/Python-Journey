# Goal: Write a recursive function that returns the sum from 1 to n.

def sum_of_numbers(n):
    if n == 1:
        return 1
    return n + sum_of_numbers(n-1)

n = int(input('Enter number: '))
print(sum_of_numbers(n))