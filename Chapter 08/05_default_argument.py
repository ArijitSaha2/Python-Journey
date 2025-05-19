def goodDay(name, ending= 'Thank you'):
    print(f"Good day, {name}")
    print(ending)

goodDay("Harry", "Thanks")
goodDay("Jackson")


def greet(name="Stranger"):  # "Stranger" is the default parameter
    print(f"Hello, {name}")

greet()           # Uses default argument "Stranger"
greet("Harry")    # Uses argument "Harry"
