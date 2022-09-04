def db_sort(arr): 
    
    n = [x for x in arr if isinstance(x , int)]
    s = [x for x in arr if isinstance(x , str)]
    
    n.sort()
    s.sort()
    
    return n + s
