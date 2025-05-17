# Mutable vs Immutable
'''Create a list and a tuple. Try modifying the first element of both. What happens and why?'''

l = [1,3,5]
l[0] = 20
print(l)

t = (2,4,7)
t[0] = 10
print(t)

'''list will have its 1st element changed since lists are mutable meaning there values can be changed and removed directly. 

tuple will show us an error since the value cannot be changed and removed as tuples are Immutable, so there values cannot be changed directly.'''