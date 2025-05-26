# Check if a number is a power of 2 using recursion.

def power(n):
    if n <= 0:
        return "Entered number is Negative or Zero"
    if n == 1:
        return True
    if n % 2 != 0 and n != 1:
        return False
    return power(n // 2)

    
n = int(input("Enter Number: "))
print(power(n))