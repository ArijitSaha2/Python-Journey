# Check if a string contains a vowel

def check_str(word):
    
    vowels = ('a','e','i','o','u')
    for ch in word:
        if ch in vowels:
            return f'{word} contains vowel'
    return f'{word} no vowels'

print(check_str('Ginger'))