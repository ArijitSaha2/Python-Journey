# Write a function max_in_list(lst) that takes a list of numbers and returns the largest number.



def max_in_list(lst):
    if lst[0] > lst[1] and lst[0] > lst[2]:
        return lst[0]
    elif lst[1] > lst[0] and lst[1] > lst[2]:
        return lst[1]
    else:
        return lst[2]
       
lst = []
n1 = int(input("Enter your number: "))
n2 = int(input("Enter your number: "))
n3 = int(input("Enter your number: "))
lst.append(n1)
lst.append(n2)
lst.append(n3)

print(lst)
print(f"The largest number in the list is {max_in_list(lst)}")