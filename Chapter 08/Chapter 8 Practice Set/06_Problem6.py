# write a python function which converts inches to cms.

def conv(inches):
    return inches * 2.54

inches  = float(input('Enter your value in inches: '))
print(f"{inches} inches is {conv(inches)} centimeters")