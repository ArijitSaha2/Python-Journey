# Check if a String is Palindrome (Ignore Case)

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(is_palindrome("racecar"))