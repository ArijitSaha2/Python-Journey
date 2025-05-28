# Print Digits Left to Right

def show_l_to_r(n):
    if n < 10:
        print(n)
        return
    show_l_to_r (n // 10)
    print(n % 10)

show_l_to_r(1234)