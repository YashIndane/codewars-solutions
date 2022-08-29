def name_in_str(str, name):
    
    str = str.lower()
    name = name.lower()
    i = 0
    for k in str : 
        
        if k == name[i] : 
             i += 1
             if i == len(name) : 
                
                return True
    return False
