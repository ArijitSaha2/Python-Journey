# WAP to accept marks of 6 students and display them in a sorted manner.

Marks = []
M1 = int(input("Enter your Marks Student 1: "))
Marks.append(M1)
M2 = int(input("Enter your Marks Student 2: "))
Marks.append(M2)
M3 = int(input("Enter your Marks Student 3: "))
Marks.append(M3)
M4 = int(input("Enter your Marks Student 4: "))
Marks.append(M4)
M5 = int(input("Enter your Marks Student 5: "))
Marks.append(M5)
M6 = int(input("Enter your Marks Student 6: "))
Marks.append(M6)

Marks.sort() 
print(Marks)
