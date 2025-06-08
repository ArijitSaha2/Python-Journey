# Write a function that checks if a number is prime or not.

def prime(n):
    if n <= 1:
        return "Not a prime number."
    if n == 2:
        return "It's a prime number."
    if n % 2 == 0:
        return "Not a prime number."
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return "Not a prime number."
    return "It's a prime number."

print(prime(0))
print(prime(1))
print(prime(2))
print(prime(17))
print(prime(18))
