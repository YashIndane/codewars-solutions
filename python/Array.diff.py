def array_diff(a, b):
    #your code here
    d = {x:0 for x in b}
    e = []
    for q in a:
        if q not in d:
            e.append(q)
    return e
