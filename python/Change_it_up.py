def changer(string):
    
    cons = 'bcdfghjklmnpqrstvwxyz'
    cons += cons.upper()
    
    vow = 'aeiouAEIOU'
    w = ''
    
    for x in string : 
        
        if x not in 'zZ' : 
            if x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
             q =  chr(ord(x) + 1) 
             if q in vow  : w += q.upper()
             elif q in cons : w += q.lower()
            else : 
                w += x
                
                
        elif x in 'Zz' : 
            w += 'A'
        
    return w
