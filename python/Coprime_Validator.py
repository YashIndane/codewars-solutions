def are_coprime(n,m):
    a, b = [x for x in range(2, n+1) if n%x==0], [x for x in range(2, m+1) if m%x==0]
    for q in a:
        if q in b:
            return False
    return True
