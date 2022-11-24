def solve(a,b):
    w=""
    for k in a:
        if k not in b:
            w += k
    for l in b:
        if l not in a:
            w += l
    return w
