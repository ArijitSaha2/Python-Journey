# Write a program to print the first 'n' multiples of a given number using a while loop.

g = int(input("Enter a number: "))

n = int(input("Enter a number: "))

i = 1

while i <= n:
    print(f"{g} x {i} = {g*i}")
    i += 1