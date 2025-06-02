# Write a program that takes a list of numbers and prints the largest and smallest number in the list.

def List():
    l = [1,99,-1]
    largest = l[0]
    smallest= l[0]
    for num in l:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    print(f'{largest} is largest number')
    print(f'{smallest} is smallest number')

List()