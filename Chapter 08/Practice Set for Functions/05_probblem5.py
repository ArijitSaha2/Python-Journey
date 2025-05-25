# Function c_to_f(celsius) that returns the temperature in Fahrenheit.
# Formula: (celsius * 9/5) + 32

def c_to_f(celsius):
    return (celsius * 9/5) + 32

celsius = float(input('Enter temperature: '))

print(c_to_f(celsius))