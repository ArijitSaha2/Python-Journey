# Write a while loop that prints the sum of digits .

n = int(input("Enter your number: "))
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10

print("Sum of digits: ", total)