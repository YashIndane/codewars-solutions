def shorter_reverse_longer(a,b):
    n, m = sorted([a, b], key=len)
    return n+m[::-1]+n  if len(a)!=len(b) else b+a[::-1]+b
