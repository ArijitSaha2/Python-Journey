# write a program to print multiplication table of n using for loops in reversed order.

n = int(input("Enter your number: "))

for i in range (10, 0, -1):      
    print(f"{n} x {i} = {n*i}")
 # This Works As well
# for i in range(1,11):
#     print(f"{n} x {11-i} = {n*(11-i)}")