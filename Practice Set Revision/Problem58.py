# Write a function that returns the sum of all numbers in a list.

def sum_all(n):
    total = 0
    for num in n:
        total += num
    return total

m = [1, 2, 3, 4]
print(sum_all(m))