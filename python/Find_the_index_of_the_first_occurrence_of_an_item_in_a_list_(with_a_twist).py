def index_finder(lst, x):
    if lst.count(x)==1:
        return lst.index(x)
    else:
        c=0
        if lst[0] == x:
            for i, j in enumerate(lst):
                if j==x and c==0:
                    c+=1
                elif j==x and c==1:    
                    return i
        else:
            return lst.index(x)
