# Write a program which finds out whether a given name is present in a list or not.

list = ['kingston','Justin','selena','Lana del rey']

Name = input('Enter Your name: ')

if(Name in list):
    print('Your name is in the list!!',Name)

else:
    print("Sadly your name is not there in the list,",Name)