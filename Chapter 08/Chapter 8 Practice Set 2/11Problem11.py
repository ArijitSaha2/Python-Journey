# Write a function print_first_last(lst) that takes a list and prints only the first and last elements.
'''Example:

print_first_last([10, 20, 30, 40, 50])'''

def _first_last(lst):
    print(f'First Item: {lst[0]}\nSecond Item: {lst[-1]}')

LIST = [10, 20, 30, 40, 50]

_first_last(LIST)