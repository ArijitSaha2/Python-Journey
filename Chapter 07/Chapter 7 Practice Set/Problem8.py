# Write a program to print the following star pattern.
"""
n = 3
*
**
***
"""

n = int(input('Enter your number: '))

for i in range(1,n+1):
    print("*"* i, end="")
    print("")