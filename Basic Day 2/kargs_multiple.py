def a_lot(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    remainder = num1 % num2
    return sum, mul, remainder


everything = a_lot(3, 2)
print(everything)


def fampus_name(first, last, **additional):
    name = f'{first}{last}'
    return name


name = fampus_name(first='Rahim', last='Boss', title='Lulu')
print(name)
