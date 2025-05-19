# Problem: Right-Angle Triangle (Descending Stars).

n = int(input("Enter your number: "))

# Outer loop to go through each row
for i in range(n, 0, -1):  # Start at n, go down to 1
    print("*" * i)  # Print i stars for the ith row
