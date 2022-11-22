def fun(str_, x):
    c = 0
    for v in range(len(x)):
        if x[v] != str_[v]:
            return c
        else: c += 1
    return c    
        
def string_suffix(str_):
    #your code here
    q = 0
    for b in range(len(str_)):
        x = str_[b:]
        q += fun(str_, x)
    return q
