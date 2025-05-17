# Positive, Negative, or Zero
'''
Take a number input.
Print whether the number is: Positive, Negative
Or Zero'''

n = int(input('Enter your number: '))

if n > 0:
    print(f"{n} is Positive")
elif n < 0:
    print(f"{n} is Negative")
else:
    print("Entered number is Zero")

# Maximum of Three Numbers
'''Take 3 numbers as input from the user.
Print which one is the largest.'''

num1 = int(input('Enter 1st Number: '))
num2 = int(input('Enter 2nd Number: '))
num3 = int(input('Enter 3nd Number: '))

if num1 > num2 and num1 > num3:
    print(f'{num1} is the greatest number.')
elif num2 > num1 and num2 > num3:
    print(f'{num2} is the greatest number.')
elif num3 > num2 and num3 > num1:
    print(f"{num3} is the greatest number.")
else:
    print("Two or more numbers are equal or invalid input.")