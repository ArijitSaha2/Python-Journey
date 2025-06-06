# Write a function that returns the largest number from a list without using the built-in max().
"""# Input: [10, 20, 5, 8]
   # Output: 20"""

def largest(lst):
    num = lst[0]
    for no in lst:
        if no > num:
            num = no
    return num
lst = [10, 20, 5, 8]
print(largest(lst))