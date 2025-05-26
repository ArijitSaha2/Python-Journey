# Check if a string is palindrome using recursion.

def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])

word = input('Enter word: ') # E.g. racecar, madam, lol
print(palindrome(word))