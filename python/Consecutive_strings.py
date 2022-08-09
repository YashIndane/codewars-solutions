def longest_consec(strarr, k):
    
    w = 0
    
    m =''
    for i in range(len(strarr) - k + 1) : 
      g = ''
      for j in range(i , i + k) : 
        g += strarr[j]
        
      if len(g) > w : 
       m = g
    
       w = len(g)
    return m
