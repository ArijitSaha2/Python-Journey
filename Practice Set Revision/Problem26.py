# Print Fibonacci up to n terms. print the first 7 numbers of this sequence.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

fibonacci(7)