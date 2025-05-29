# Print numbers from 1 to n in for loop using function.

def num(n):
    if n == 0:
        return
    for i in range(1, n+1):
        print(i)

n = int(input('Enter number: '))
num(n)


'''      Same Program Done Recursively
def num(n):
    if n == 0:
        return
    num(n-1)
    print(n)

num(5)'''