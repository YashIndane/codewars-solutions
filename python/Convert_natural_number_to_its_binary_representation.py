def int_to_bin(n):
    z = str(bin(n))
    z = z.replace('0b' , '')
    return z
