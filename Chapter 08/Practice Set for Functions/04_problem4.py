# Function max_of_two(a, b) that returns the bigger number.

def max_of_two(a, b):
    if a == b:
        return("Both Numbers are equal")
    if a < 0 or b < 0:
        return("Negative Numbers are not allowed")
    if a > b:
        return(f"{a} is bigger than {b}")
    if b > a:
        return(f"{b} is bigger than {a}")

a = int(input("Enter number: "))
b = int(input("Enter number: "))
print(max_of_two(a, b))