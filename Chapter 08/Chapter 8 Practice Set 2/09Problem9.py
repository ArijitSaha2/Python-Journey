# Write a function same_string(s1, s2) that returns True if both strings are the same, otherwise False.

def same_string(s1, s2):
    return s1 == s2

str1 = input('Enter str1: ')
str2 = input('Enter str2: ')
print(same_string(str1, str2))