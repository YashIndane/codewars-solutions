def automorphic(n):
    a = len(str(n))
    q = str(n**2)
    a1 = len(q)
    
    
    return 'Automorphic' if str(n) == q[a1 - a:] else 'Not!!'
