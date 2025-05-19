# Write a program to find out whether a student is passed or fails, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take mark as an input from the user.

mark1 = int(input('Enter your marks1:'))
mark2 = int(input('Enter your marks2:'))
mark3 = int(input('Enter your marks3:'))

total_percentage = (mark1+mark2+mark3)/300*100

if(total_percentage>=40 and mark1>=33 and mark2>=33 and mark3>=33):
    print('You Pass', total_percentage)
else:
    print('You fail', total_percentage)