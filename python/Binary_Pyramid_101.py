def binary_pyramid(m,n):
    return bin(sum([int(bin(v).replace('0b', '')) for v in range(m, n+1)])).replace('0b', '')
