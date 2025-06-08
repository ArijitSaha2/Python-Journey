# Write a function that takes a string and returns the reversed version of it.

def rever(word):
    if len(word) <= 1:
        return word 
    return word[::-1]

print(rever('polarbear'))