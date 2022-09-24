def compute_sum(n):
    if n < 10:
        return n*(n+1)//2
    else:
        w = 0
        for x in range(10, n+1):
            w += sum(map(int, str(x)))
        return 45+w
