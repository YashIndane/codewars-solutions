def factorsRange(n, m):
    
    d = {}
    for k in range(n , m + 1) : 
         j = [v for v in list(range(2 , k)) if k % v == 0]
         if len(j) == 0 :  d[k] = ['None']  
         else :    
           d[k] = j
    return d
