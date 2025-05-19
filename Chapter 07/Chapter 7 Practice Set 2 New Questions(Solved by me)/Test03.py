# Calculate the sum of the first n natural numbers using a loop.

n = int(input("Enter your Number: "))

sum = 0

i = 1

for i in range(1, n+1):
    sum = sum + i
    i += 1

print(f"{sum}")
    