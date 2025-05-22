# Write a function that takes a list of numbers and returns the sum. Use a loop, not sum().

def list_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

Listt = []
Num1 = int(input('Enter Number: '))
Num2 = int(input('Enter Number: '))
Num3 = int(input('Enter Number: '))
Listt.append(Num1)
Listt.append(Num2)
Listt.append(Num3)

print(list_sum(Listt))