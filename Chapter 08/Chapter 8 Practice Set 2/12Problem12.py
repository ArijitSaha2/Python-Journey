# Write a function that returns the length of the string s. Don't use len().

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

word = input('Enter your word: ')
print(string_length(word))