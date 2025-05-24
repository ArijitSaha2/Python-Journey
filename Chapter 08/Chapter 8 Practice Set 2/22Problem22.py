# Write a recursive function to print all natural numbers from 1 to n.
'''
Example:
Input: 5
Output: 1 2 3 4 5     '''

def print_natural(n , current = 1):
    if current > n:
        return
    print(current, end = "")
    print_natural(n, current+1)

print_natural(5)