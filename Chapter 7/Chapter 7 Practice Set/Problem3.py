# Attempt problem 1 using while loop.

n = int(input("Enter Your Number: "))

i = 1

while i < 11:  # while i in range(1, 11) can be used as well. 
    print(f"{n} x {i} = {n * i}")
    i += 1