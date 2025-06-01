# Count vowels in a string
# Input: "Hello World"



def count_vowel(word):
    vowels = ('a','e','i','o','u')
    count = 0
    for ch in word.lower():
        if ch in vowels:
            count += 1
    return count

print(count_vowel("Hello World"))