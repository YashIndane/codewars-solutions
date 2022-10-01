def nb_dig(n, d):
    return sum([str(x**2).count(str(d)) for x in range(0, n+1)])
