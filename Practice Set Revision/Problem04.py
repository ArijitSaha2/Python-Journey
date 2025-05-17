# Problem 3: Positive, Negative, or Zero
"""Task:
Write a program that takes an integer input and prints:
'Positive' if the number > 0
'Negative' if the number < 0
'Zero' if it equals zero"""

n = int(input("Enter your number: "))

if n > 0:
    print('Positive')
elif n < 0:
    print('Negative')
else:
    print('Zero')