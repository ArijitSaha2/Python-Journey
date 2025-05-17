# Voting Eligibility Checker
'''Take the user's age as input.
Print:
"You are eligible to vote" if age is 18 or above.
"Not eligible to vote" otherwise.'''

age = int(input("Enter your age: "))
if age >= 18:
    print("Your Eligible to Vote")
elif age < 18:
    print("Not Eligible to vote")

# Grading System
'''Take a marks input (0 to 100).
Print grades:
90-100 → A, 80-89 → B, 70-79 → C, 60-69 → D, Below 60 → F
If marks are not in the 0-100 range, print "Invalid Marks".'''

marks = int(input("Enter your Marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
