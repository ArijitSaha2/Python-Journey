# Print "Hello" n times

def greet(n):
    if n == 0:
        return 
    print("Hello")
    return greet(n-1)

greet(4)