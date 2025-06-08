# Write a function that returns the second largest number in a list without using built-in max() or sort().

def great(n):
    largest = float('-inf')
    second_large = float('-inf')

    for num in n:
        if num > largest:
            second_large = largest
            largest = num
        elif num > second_large and num != largest:
            second_large = num

    return f"{second_large} is the second largest number."

lst = [40, 500, 90, 10]
print(great(lst))
