# Write a function that takes a list of numbers and returns a new list with the

def new_sqr():
    m = [1,2,3,4]
    n = []
    for lst2 in m:
        lst2 = lst2 ** 2
        n.append(lst2)
    print(n)

new_sqr()