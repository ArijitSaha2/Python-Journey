# Escape Sequence Characters: These are special sequences in Python strings that start with a backslash (\) followed by one or more characters. 
# Although they are written using multiple characters in the code, Python interprets each escape sequence as representing a single character within the string.
# They are used to include characters that are difficult to type directly (like tabs or newlines) or have special meaning within strings (like quotes or backslashes themselves).

a = "i am great"
a = "i am great \nbut\\also\t\'lazy\'" # \n = NewLine; \t = Gives space like if u click tab. 
                                         # \\ = Creates a \ between two words.
                                         # \' = Put the word inside it in Quotations. REMEMBER ' and " Matters alot.
a = a.capitalize()
a = len(a)
print(a)


"i am great \nbut\\also\t\'lazy\'"