# Write a program to print multiplication table of a give number using for loop.

n = int(input("Enter your number: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
