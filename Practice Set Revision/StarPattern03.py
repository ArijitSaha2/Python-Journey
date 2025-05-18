# Pattern 3: Right-Aligned Triangle
'''Input: 4
   *
  **
 ***
****          '''

n = int(input("Enter your number: "))

for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*i, end="")
    print("")