# Fibonacci Sequence using recursion.

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(7):
    print(fib(i), end =' ')