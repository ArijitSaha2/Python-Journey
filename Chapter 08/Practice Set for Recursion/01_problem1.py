# Use recursion to print numbers from n to 1.

def reversed_order(n):
    if n == 0:
        return
    print(n)
    return reversed_order(n-1)

n = int(input('Enter number: '))
reversed_order(n)