# Pattern 1: Right-Angled Triangle
'''Input: 4
*
**
***
****'''

n = int(input("Enter your number: "))

for i in range(1, n+1):
    print("*"*i, end="")
    print("")