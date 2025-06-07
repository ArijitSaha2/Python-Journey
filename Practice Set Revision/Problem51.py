# Write a function that takes a number n and prints all numbers from 1 to n.

def numbers(n):
    if n == 0:
        return
    numbers(n-1)
    print(n)
    
nom = int(input('Enter number: '))
numbers(nom)