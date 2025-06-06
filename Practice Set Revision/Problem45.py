# Write a function that counts how many words are in a sentence.

def count_words(word):
    return len(word.split())

print(count_words("Hello world"))