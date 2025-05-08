# Write a program to determine if a customer qualifies for a special discount. A customer qualifies if they meet either of the following conditions:

    # They are a premium member AND they have spent more than ₹1000 in a single purchase.
    # They are a regular member AND they have spent more than ₹5000 in a single purchase.

a = int(input("Enter your total price: "))

b = input("Enter your Shop ID: ")

c = 'Premium' # shop ID
d = 'Regular' # shop ID

if(b==c and a>1000):
    print('Your Eligible for Discount.')
elif(b==d and a>5000):
    print('Your Eligible for discount.')
elif(b==c and a<1000):
    print('Shop more homies your almost there.')
elif(b==d and a<5000):
    print('Your not eligible')
else:
    print('Please enter a valid Shop ID.')