# Check Even or Odd
# Function is_even(n) that returns True if the number is even, else False.

def is_even(n):
    if n % 2 == 0:
        print(f"{n} is even.")
    else:
        print(f"{n} is odd")

n = int(input('Enter your number: '))

is_even(n)