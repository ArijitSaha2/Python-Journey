# Predict Output (Tracing):

def mystery(n):
    if n <= 0:
        return
    print(n)       # Step 1
    mystery(n - 2) # Step 2: Recursive call
    print(n)       # Step 3: After recursion
mystery(4)

'''Predicted Output/Answer: 
4
2
2
4
'''