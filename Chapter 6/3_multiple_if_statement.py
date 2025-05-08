a = int(input("Enter your Age: "))

# If statement number 1
if(a%2 == 0):
    print("a is Even")
# End of If Statement number 1

# If statement number 2
if(a>=18):
    print("Your Above the age of Consent")
    print("Good For You")

elif(a<0):
    print('Your Entering an Invalid age in Negative')

else:
    print("Your below the age of Consent")
# Ending of If statement number 2
print('End of program')



# Great example of if inside an if(nested if statements)
'''
age = int(input("Enter your age: "))

if age > 0:  # Outer if: Check if the age is positive
    print("Your age is valid.")
    if age >= 18:  # Inner if: Check if the age is 18 or older
        print("You are an adult.")
    else:  # Inner else: If the outer if was true but the inner wasn't
        print("You are a minor.")
else:  # Outer else: If the initial age check failed
    print("Invalid age.")
'''