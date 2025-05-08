#  Write a program to find whether a given username contains less than 10 characters or not.

a = input('Enter your username: ')

if(len(a)<10):
    print("Username contains less then 10 characters",a,len(a))

else:
    print('Username Has sufficient characters',a,len(a))
