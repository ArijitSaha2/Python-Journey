# Pattern: Number Pyramid
"""
Input: 5
Output:
1
22
333
4444
55555
"""

n = int(input("Enter your Value: "))

for i in range(1, n+1):
    print(str(i)*i, end="")
    print("")