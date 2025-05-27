# Count down from n to 1

def count_down(n):
    if n == 0:
        return 1
    print(n)
    return count_down(n - 1)

count_down(5)