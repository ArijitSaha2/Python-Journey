# Problem 5: Grading System
'''Task:
Write a program that takes marks (0-100) as input and prints the grade based on the following criteria:
90-100 → Grade A
80-89 → Grade B
70-79 → Grade C
60-69 → Grade D
0-59 → Grade F
Anything outside 0-100 → Print "Invalid Marks"'''

n = int(input("Enter your Marks: "))

if n < 0 or n > 100:
    print("Invalid")
elif n >= 90:
    print("Grade A")
elif n >= 80:
    print("Grade B")
elif n >= 70:
    print("Grade C")
elif n >= 60:
    print("Grade D")
else:
    print("Grade F")
