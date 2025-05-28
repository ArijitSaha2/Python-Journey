# Check Even or Odd using recursion

def even_or_odd(n):
    if n == 0:
        return "even"
    elif n == 1:
        return "odd"
    return even_or_odd(n-2)    
n = int(input('Enter number: '))
print(even_or_odd(n))