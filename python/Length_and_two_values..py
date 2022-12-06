def alternate(n, first_value, second_value):
    w=[]
    for x in range(0,n):
        w.append(first_value)
        w.append(second_value)
    return w[:n]
