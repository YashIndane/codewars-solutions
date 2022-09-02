def square_digits(num):
    num = str(num)
    return int(''.join([str(int(x) ** 2) for x in num]))
