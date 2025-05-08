# If else and elif statements are a multiway decision taken by our program due to certain conditions on our code.

a = int(input("Enter your Age: "))

# if elif else ladder

if(a>=18):
    print("Your Above the age of Consent")
    print("Good For You")

elif(a<0):
    print('Your Entering an Invalid age in Negative')

elif(a==0):
    print('Your Entering Invalid age that is 0')

else: 
    print("Your below the age of Consent") # The final Else statement executes only when other conditions are not met.

print('End of program')