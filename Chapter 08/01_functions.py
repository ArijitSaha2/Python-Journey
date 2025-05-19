'''A function is a group of statements performing a specific task.

When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track on which piece of code is doing what!

A function can be reused by the programmer in a given program any number of
    --EXAMPLE AND SYNTAX OF A FUNCTION--

The syntax of a function looks as follows:
Python

def func1():
    print('hello')

This function can be called any number of times, anywhere in the program.

--FUNCTION CALL--

Whenever we want to call a function, we put the name of the function followed by parentheses as follows:
Python

func1() 

'''
# Function Definition
def avg(): # Syntax for function call
    a = int(input("Enter your Number: ")) 
    b = int(input("Enter your Number: "))
    c = int(input("Enter your Number: "))

    average = (a + b + c) / 3

    print(average)

avg() # Function Call
print("Thank you")
avg() 
avg()