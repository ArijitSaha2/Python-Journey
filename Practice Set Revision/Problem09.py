# Print a right-angled star triangle of height N (user input).
'''
   * n = 3
  ** => Self Reference
 ***
 '''

n = int(input("Enter your Number: "))

for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*i, end="")
    print("")
