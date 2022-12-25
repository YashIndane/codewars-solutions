import itertools
def sum_consecutives(s):
    #good luck
    q=[]
    s=itertools.groupby(s)
    for a,b in s:
        q.append(a*len(list(b)))
    return q
