def sum_mul(n, m):
    if n < 1 or m < 1:
        return "INVALID"
    else:
        s=0
        for x in range(1,1000000):
            p=x*n
            if p<m:
                s+=p
            else:
                return s
