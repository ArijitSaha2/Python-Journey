# Sum of first n natural numbers

def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum(10))

# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n-1)

# print(sum(10))