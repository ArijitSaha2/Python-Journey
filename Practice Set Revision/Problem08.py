# List Input & Print
'Take 5 numbers from user, store in list, print the list.'

l = []

for i in range(1,6):
    n = int(input(f"Enter your Number {i}: "))
    l.append(n)

print(l)