# Write a function that multiplies all the numbers in a list.

def mult(lst):
    result = 1
    for num in lst:
        result *= num
    return result
    
print(mult([2,3,4]))