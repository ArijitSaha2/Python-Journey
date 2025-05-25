# Function is_vowel(ch) that returns True if it's a vowel, else False.

def is_vowel(ch):
    return ch.lower() in ('a','e','i','o','u')


ch = input('Enter word: ')
print(is_vowel(ch))