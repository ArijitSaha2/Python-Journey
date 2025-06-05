# Write a function that takes a string and returns the number of vowels in it.

def check_vowels(word):
    count = 0
    for ch in word.lower():
        if ch in 'aeiou':
            count += 1
    return count
        
print(check_vowels('Education'))