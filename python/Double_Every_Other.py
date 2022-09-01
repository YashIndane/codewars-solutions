def double_every_other(lst):
    
    w = []
    for i , k in enumerate(lst) :  w.append(k*2 if i % 2 == 1 else k)
    return w
