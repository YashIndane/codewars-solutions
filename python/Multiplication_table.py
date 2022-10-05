def multiplication_table(size):
    q = []
    w = list(range(1, size+1))
    for f in range(1, size+1):
        q.append([x*f for x in w])
    return q
