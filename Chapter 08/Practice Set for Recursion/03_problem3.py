# Print numbers from 1 to n using recursion.

def forward_count(start, n):
    if start > n:
        return
    print(start)
    return forward_count(start + 1, n)

forward_count(1, 10)