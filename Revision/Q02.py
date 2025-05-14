# Write a while loop that prints the reverse of a number.
"""Example:
Input: 1234
Output:
4
3
2
1
"""
n = int(input("Enter your numbers: "))

while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10