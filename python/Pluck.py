def pluck(objs, name): 
    # your code here
    q=[]
    for x in objs:
        try:
            q.append(x[name])
        except:
            q.append(None)
            continue
    return q
