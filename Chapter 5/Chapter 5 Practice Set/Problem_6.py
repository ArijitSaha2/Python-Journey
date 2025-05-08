# Create an empty dictionary. Allow 4 friends to enter their favourite language as value and use key as their names. Assume that the names are unique.

name = {}

name1 = input("Enter your Name: ")
Lang1 = input("Enter Your Favourite language: ")
name.update({name1:Lang1})

name2 = input("Enter your Name: ")
Lang2 = input("Enter Your Favourite language: ")
name.update({name2:Lang2})

name3 = input("Enter your Name: ")
Lang3 = input("Enter Your Favourite language: ")
name.update({name3:Lang3})

name4 = input("Enter your Name: ")
Lang4 = input("Enter Your Favourite language: ")
name.update({name4:Lang4})

print(name)