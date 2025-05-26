# Write a recursive function that prints "hi" exactly n times.
# No loops. Just recursion.

def say_hi(n):
    if n == 0:
        return
    print('hi')
    return say_hi(n-1)

say_hi(5)