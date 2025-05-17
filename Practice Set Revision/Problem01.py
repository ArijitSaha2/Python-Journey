# Modules & datetime
'''Write a program that imports the datetime module and  prints:
Current date and time
Only the current year extracted from the datetime object'''

from datetime import datetime 

today = datetime.now()

print(today.year)