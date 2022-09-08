def accum(s):
    # your code
    w = ""
    for i, x in enumerate(s):
        w += x.upper() + x.lower()*i + "-"
    return w[:len(w)-1]
