def digitize(n):
    w = [x for x in str(n)]
    w = [int(x) for x in w]
    w.reverse()
    return w
