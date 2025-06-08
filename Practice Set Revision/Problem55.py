# Write a function that takes a string and a character, and returns how many times the character appears in the string.

def count_ap(word, character):
    count = 0
    for ch in word:
        if ch == character:
            count += 1
    return count


print(count_ap('Banana', 'a'))