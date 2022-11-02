def dup(arry):
    w=[]
    for x in arry:
        temp=""
        for k in x:
            if not temp.endswith(k):
                temp+=k
        w.append(temp)        
    return w
