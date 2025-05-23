# Simple recursive function to print numbers from m down to 1

def countdown(m):
    if m == 0:
        return
    print(m)
    countdown(m-1)

num = int(input("Enter number: "))
countdown(num)