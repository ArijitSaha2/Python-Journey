# Pattern 2: Inverted Right-Angled Triangle
'''Input: 4
****
***
**
*         '''

n = int(input("Enter your number: "))

for i in range(0, n):
    print("*"*(n-i), end="")  # n = 5 since n+1
    print("")