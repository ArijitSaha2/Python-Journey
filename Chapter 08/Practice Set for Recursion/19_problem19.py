# Palindrome

def palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])

print(palindrome('lol'))