# Write a function reverse_string(s) that returns the reverse of the string s.

def reverse_string(s):
    if len(s) < 1:
        return s
    return reverse_string(s[1:]) + (s[0])

word_to_be_reversed = input('Enter word: ')
print(reverse_string(word_to_be_reversed))