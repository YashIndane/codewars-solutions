def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    
    #x-y
    x=max(a1, key=lambda i: len(i))
    y=min(a2, key=lambda i: len(i))
    
    #y-x
    x_=max(a2, key=lambda i: len(i))
    y_=min(a1, key=lambda i: len(i))
    
    return max([abs(len(x_)-len(y_)), abs(len(x)-len(y))])
