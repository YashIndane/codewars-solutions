from itertools import groupby
def get_consective_items(items, key): 
    # your code here
    s=str(items)
    key=str(key)
    if key in s:
        w=groupby(s)
        z=0
        for a,b in w:
            if a==key:
                z=max(z, len(list(b)))
        return z           
    else:
        return 0
