# Print numbers in reverse using recursion
# Input: 5 → Output: 5 4 3 2 1

def reverse_print(n):
    if n == 0:
        return 
    print(n, end="")
    reverse_print(n-1)

reverse_print(5)