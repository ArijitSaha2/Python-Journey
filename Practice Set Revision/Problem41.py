# Write a function that returns the factorial of a given number using a loop.

def fact(n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result

n = int(input('Enter number: ')) 
print(fact(n))