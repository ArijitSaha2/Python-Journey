# Write a Python function to remove a given word from a list and strip at the same time.

def rem(my_list, word):
    n = []
    for item in my_list:
        if item != word:
            n.append(item.strip(word))
    return n

l = ["Harry", "Rohan", "Shubham", "an"]
print(rem(l, "an"))