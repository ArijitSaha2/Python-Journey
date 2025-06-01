# Check if a number is a perfect square

def perfect(n):
    sqrt = int(n ** 0.5)
    if sqrt * sqrt == n:
        return True
    else:
        return False
    
print(perfect(9))