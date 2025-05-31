# Print All Factors of a Number
# Input: n = 12
# Output: 1 2 3 4 6 12

n = 12
f = []
for i in range(1, n+1):
    if n % i == 0:
        f.append(i)

print(f'{f} are the factors of {n}')