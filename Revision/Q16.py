# Write a program that:
'''Takes a number as input.
Prints all numbers from 1 to that number (inclusive), using a while loop.'''

n = int(input('Enter your number: '))
i = 1

while i <= n:
    print(i)
    i += 1

# Write a program that:(COMMENT OUT THE ABOVE CODE TO AVOID CONFUSION)
'''Uses a for loop to print all even numbers from 1 to 20.'''

for i in range(1, 20,):
    if i % 2 == 0:
        print(i)
