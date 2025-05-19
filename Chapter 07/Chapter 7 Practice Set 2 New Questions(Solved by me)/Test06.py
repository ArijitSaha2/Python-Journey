# Problem: Count the number of digits in a number using a while loop.

n = int(input("Enter your number: "))
C = 0
while n > 0:
    n = n // 10
    C += 1

print(C)