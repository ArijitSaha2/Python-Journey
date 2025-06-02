# Write a program to check if a given number is even or odd using the modulus operator.

def is_even(n):
    if n < 0:
        print("Positive Numbers only!!")
    elif n % 2 == 0:
        print("It is Even")
    else:
        print("It is Odd")
n = int(input("Enter Number: "))
is_even(n)


# Write a program that asks the user for their age and prints whether they are a minor, adult, or senior citizen.

def age(num):
    if num < 1:
        print("Invalid Age")
    elif num < 18:
        print("You're a Minor")
    elif num >= 18 and num < 60:
        print("You're an Adult")
    elif num >= 60:
        print("You're a Senior Citizen")

num = int(input('Enter Age: '))
age(num)