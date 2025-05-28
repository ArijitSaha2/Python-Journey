# Reverse a String using recursion 

def reverse_str(word):
    if len(word) == 0:
        return ""
    return reverse_str(word[1:]) + word[0]

print(reverse_str('Good'))