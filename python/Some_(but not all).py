def some_but_not_all(seq, pred): 
    # your code here
    l=list(filter(pred, seq))
    if len(l) == len(seq): return False
    elif len(l)<len(seq) and len(l)>0: return True
    else:
        return False
