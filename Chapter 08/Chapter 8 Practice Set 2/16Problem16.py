# Predict the Output

def trace(x):
    if x == 1:
        return
    print("A", x) # Prints 1st
    trace(x - 1)  # Recursive Call
    print("B", x) # Prints after Recursion Call is complete 
trace(3)

'''
Predicted Output/Answer:
A 3
A 2
B 2
B 3
'''