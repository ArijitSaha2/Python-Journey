# Loops
'''Using while, print numbers 1 to N (user input).
Using for, print even numbers from 1 to 20.'''

n = int(input("Enter a Number: "))

i = 1

while i <= n:
    print(i)
    i += 1

for j in range(1, 20):
    if j % 2 == 0:
        print(j)

# Comment out 1 loop to avoid confusion