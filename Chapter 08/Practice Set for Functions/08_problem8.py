# Absolute Value
# Function absolute(n) that returns the absolute value of a number (without using abs()).

def absolute(n):
    if n < 0:
        return n * -1
    else:
        return n

n = int(input('Enter number: '))
print(absolute(n))