# Write a program to find whether a given number is prime or not.

n = int(input("Enter your Number: "))

for i in range(2, n):
    if(n%i) == 0:
        print(f"{n} is not prime")
        break
else:
    print(f"{n} is a prime number")

