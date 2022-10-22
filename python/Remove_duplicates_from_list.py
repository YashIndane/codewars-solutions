def distinct(seq):
    d={}
    w=[]
    for x in seq:
        if x not in d:
            w.append(x)
            d[x]=0
    return w 
