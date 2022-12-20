def smallest_product(a):
    q=[]
    for x in a:
        a=1
        for c in x:
            a*=c
        q.append(a)
    return min(q)
