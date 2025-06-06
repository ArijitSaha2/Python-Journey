# Write a function to check if a string is a palindrome.

def check_pal(word):
    word = word.lower()
    if len(word) <= 1:
        return "It's a palindrome"
    if word[0] != word[-1]:
        return "It's not a palindrome"
    return check_pal(word[1:-1])

print(check_pal('racecar'))