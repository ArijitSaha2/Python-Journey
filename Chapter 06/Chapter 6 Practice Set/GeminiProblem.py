# Write a program that takes three numbers as input from the user and prints "All numbers are equal" if all three numbers are the same, otherwise it prints "Numbers are not all equal".

a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))
c = int(input("Enter a Number: "))

if(a==b and b==c and c==a):
    print("All numbers are equal")
else:
    print("Numbers are not all equal")