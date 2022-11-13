from math import prod
def per(n):
    if len(str(n)) < 2:
        return []
    else:
        q = []
        while len(str(n)) != 1:
            w = prod(list(int(c) for c in str(n)))
            q.append(w)
            n=w
        return q
