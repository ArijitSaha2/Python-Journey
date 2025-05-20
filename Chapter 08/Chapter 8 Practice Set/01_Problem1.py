# write a program using functions to find the greatest of three numbers.

def max(n, n1 , n2):
    if n > n1 and n > n2:
        return n
    if n1 > n and n1 > n2:
        return n1
    if n2 > n and n2 > n1:
        return n2
    
n = int(input("Enter 1st number: "))
n1 = int(input("Enter 2nd number: "))
n2 = int(input("Enter 3rd number: "))

print(f"The Greatest number is {max(n, n1, n2)}")