def search(budget,prices):
    x = []
    for c in prices : 
         if c <= budget : x.append(c)
    
   
    x.sort()
    x = [str(v) for v in x ]
    u = ','.join(x)
    return u
