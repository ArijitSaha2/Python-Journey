name = 'harry'

print(len(name))
print(name.startswith('ha'))
print(name.endswith('rry'))
print(name.capitalize())

# 1] len () function — This function returns the length of the strings.
# len("Harry") # returns 5(Btw this is done in REPL)

'''2] String.endswith("rry") — This function_ tells whether the variable string ends with the string "rry" or not. 
if string is "harry", it returns true for "rry" since Harry ends with rry.'''

# 3] string.count("c") — counts the total number of occurrences of any character.
'''string = " abracadabra "
count = string.count("c")
print(count) # Output: 1'''

# 4] string.capitalize()— this function capitalize the first character of a given string.
'''s = "hello world"
capitalized_string = s.capitalize()
print(capitalized_string) # Output: "Hello world" '''

# 5] string.find(word) — This function friends a word and returns the index of first occurrence of that word in the string.
'''s = "hello world"
index = s.find("world")
print(index) # Output: 6'''

# 6] string.replace (old word, new word ) — This function replace the old word with new word in the entire string.
s = "hello world"
s = s.replace("world","Python")
print(s) # Outout: "hello Python"

change = 'TheEldenLordwasOnceAgreatLord'
replace = change.replace('Lord','GOD')
print(replace)

# 7] string.lower(): This function returns a new string where all the characters in the original string are converted to lowercase.
text = "Hello World"
lower_text = text.lower()
print(lower_text)  # Output: "hello world"

# 8] string.upper(): This function is the opposite of .lower(). It returns a new string where all the characters in the original string are converted to uppercase.
text = "Hello World"
upper_text = text.upper()
print(upper_text)  # Output: "HELLO WORLD"