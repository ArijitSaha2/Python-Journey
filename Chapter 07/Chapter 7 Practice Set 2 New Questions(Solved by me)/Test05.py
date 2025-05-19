# Write a Python program that prints the sum of digits of a number using a while loop.

n = int(input("Enter your number: "))
i = 1
sum = 0
while i in range(1, n+1):
    sum = sum + i
    i += 1

print(f"{sum}")