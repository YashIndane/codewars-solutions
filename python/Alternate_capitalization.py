def capitalize(s):
    
    w = ''
    t = ''
    for i , k in enumerate(s) : 
        
        if i % 2 == 0 : 
            w += k.upper()
            t += k.lower()
        else : 
            t += k.upper()
            w += k.lower()
    return [w , t]
