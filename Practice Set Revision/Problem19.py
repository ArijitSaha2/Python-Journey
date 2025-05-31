# Check if a Number is Even or Odd


def is_even(n):
    if n % 2 == 0:
        return f'{n} is even'
    else:
        return f'{n} is odd'
    
print(is_even(int(input('Enter number: '))))


# n = int(input('Enter number: '))

# if n % 2 == 0:
#     print(f'{n} is even')
# elif n % 2 != 0:
#     print(f'{n} is odd')