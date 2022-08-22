def next_letter(s):
    p = ''
    for x in s : 
        
        if x != ' ' and x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' :
            
            if x == 'z' : p += 'a'
            elif x == 'Z' : p += 'A'
            else :     
               p += chr(ord(x) + 1)
        else : p += x 
    return p
