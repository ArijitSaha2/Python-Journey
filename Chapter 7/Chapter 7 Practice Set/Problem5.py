# write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter your number: "))
i = 1
s = 0
while i<=n:
    s += i
    i += 1
   
print(f"Sum of natural numbers {s}")