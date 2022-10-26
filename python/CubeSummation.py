def cube_sum(n, m):
    if n==m:
        return 0
    ma=max([n,m])
    mi=min([n, m])
    return sum([x**3 for x in range(mi+1, ma+1)])
