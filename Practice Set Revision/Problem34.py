# Write a function that takes a string and returns the number of vowels (a, e, i, o, u) in it.

def vow(word):
    count = 0
    for ch in word.lower():
        if ch in 'aeiou':
            count += 1
    return count

print(vow('hello world'))