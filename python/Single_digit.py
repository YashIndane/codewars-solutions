def single_digit(n):
    # do stuff
    s = 0
    while len(str(n)) != 1:
        s = bin(n).count('1')
        n = s
    return n
