# What is the difference between while and for loops in Python?
'''Explain this in your own words. Include:
When would you use a while loop?
When would you prefer a for loop?'''

"""
Use a 'while' loop when you don't know in advance how many times you'll iterate — it depends on a condition.

Use a 'for' loop when you do know the number of iterations — typically when looping over a range or a collection.
"""

# Predict the output and explain:
i = 1
while i <= 5:
    print(i)
    i += 1

"It will print the numbers 1 to 5, one per line, because the loop starts at 1 and runs until i exceeds 5."

# Predict the output and explain:
for j in range(3):
    print("Python")

"It will print 'Python' three times since range(3) generates 0, 1, 2 — three total iterations."