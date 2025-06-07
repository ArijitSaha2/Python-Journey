# Write a function that takes a single character and returns whether it's a vowel or consonant.

def check_vowel(alphabet):
    vowels = 'aeiou'
    alphabet = alphabet.lower()
    if alphabet in vowels:
        return "Vowel"
    else:
        return "Consonant" 

alpha1 = input('Enter 1 alphabet: ')
print(check_vowel(alpha1))