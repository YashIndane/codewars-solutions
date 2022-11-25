def geometric_sequence_elements(a, r, n):
    # Yourcode here!
    w = str(a)
    for x in range(0, n-1):
        p = a*r
        w += ", " + str(p)
        a=p
    return w
