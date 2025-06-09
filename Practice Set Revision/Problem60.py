# Write a function that counts how many vowels are in a string.

def vowel_count(word):
    vowels = "aeiou"
    count = 0
    word = word.lower()
    for ch in word:
        if ch in vowels:
            count += 1
    return count

print(vowel_count("Education"))
