# Write a function that checks if a string is a palindrome

def palindrome(word):
    word = word.lower()
    if len(word) <= 1:
        return "Its Palindrome"
    if word[0] != word[-1]:
        return "Its not a palindrome"
    return palindrome(word[1:-1])

print(palindrome('Lol'))