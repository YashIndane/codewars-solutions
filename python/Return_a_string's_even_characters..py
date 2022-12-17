def even_chars(st): 
    # your code here
    if len(st) > 100 or len(st) < 2:
        return "invalid string"
    else:
        w=[]
        for i, x in enumerate(st):
            if (i+1)%2==0:
                w.append(x)
        return w
