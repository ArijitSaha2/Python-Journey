# What will be the length of the following set S:

s = set()
s.add(20)
s.add(20.0)
s.add('20') # Sets treat 20 and 20.0 as the same value, but '20' as different due to its string type, resulting in a length of 2.

print(len(s)) 


# For set membership, Python considers the numerical value.
# Thus, the integer 20 and the float 20.0 are treated as the same.
# However, the string '20' is distinct due to its different type.
# The final length of the set is 2.