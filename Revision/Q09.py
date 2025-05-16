# What’s the purpose of using modules in Python?

'''
Reuse code — no need to write everything from scratch (e.g., math, random, datetime).

Access extra functionality — like file I/O, date/time, networking, etc., that's not built into the core language.'''

# What is the datetime module used for?

''' 
It is can be used in code to view current time, date and year respectively based on the requirement or all at once if needed .'''

# Write code that:
'''Imports the datetime module
Prints the current date and time
Extracts only the current year'''

from datetime import datetime 

now = datetime.now()

print(now)
print(now.year)
