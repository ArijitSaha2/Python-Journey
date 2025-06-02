# Problem 27: Explanation for Problem 26 (Fibonacci Sequence): 

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
        # The values in quotes show what 'a' is assigned at each step for clarity:
        # a, b = '1', 0 + 1 = 1, 1   -> here a becomes 1 (printed next loop)
        # a, b = '1', 1 + 1 = 1, 2   -> a = 1
        # a, b = '2', 1 + 2 = 2, 3   -> a = 2
        # a, b = '3', 2 + 3 = 3, 5   -> a = 3
        # a, b = '5', 3 + 5 = 5, 8   -> a = 5
        # a, b = '8', 5 + 8 = 8, 13  -> a = 8
    print() # newline after sequence
fibonacci(7)

# Raw ouput  = 0 1 1 2 3 5 8