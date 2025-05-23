# Pattern with Recursion

# Print this star pattern using recursion (no loops):
'''
*
* *
* * *
* * * *     '''

def star(n):
    if n >= 5:
        return
    print("* "*n)
    star(n + 1)    

star(1)