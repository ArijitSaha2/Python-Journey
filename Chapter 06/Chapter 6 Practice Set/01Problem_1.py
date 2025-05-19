# Write a program to find the greatest of four numbers entered by the user.

a = int(input('Enter your number: '))
b = int(input('Enter your number: '))
c = int(input('Enter your number: '))
d = int(input('Enter your number: '))

if (a>b) and (a>c) and (a>d):
    print("a is the greatest number: ",a)
if (b>a) and (b>c) and (b>d):
    print("b is the greatest number: ",b)
if (c>a) and (c>b) and (c>d):
    print("c is the greatest number: ",c)
if (d>a) and (d>b) and (d>c):
    print("d is the greatest number: ",d)
