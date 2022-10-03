from itertools import groupby
def uniq(seq): 
    # your code here
    w = groupby(seq)
    d = []
    for i, j in w:
        d.append(i)
    return d
