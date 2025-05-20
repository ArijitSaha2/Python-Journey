# write a python program using function to convert celsius to fahrenheit.

def temperature(c):
    f = (c * 9/5) + 32 # Formula for C to F
    # c = 5 * (f - 32) / 9 (Formula for F to C)
    return f

c = int(input("Enter temperature in °C to convert to °F: "))

print(temperature(c))