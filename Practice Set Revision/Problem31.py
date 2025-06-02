# Chapter 5 (Loops):
# Write a program to print the first 10 natural numbers using a while loop.

def natural():
    i = 1
    while i <= 10:
        print(i)
        i += 1

natural()


# Chapter 6 (Strings):
# Write a program to check if a given string is a palindrome.

def palindrom(word):
    word = word.lower()
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrom(word[1:-1])
    
print(palindrom("Racecar"))