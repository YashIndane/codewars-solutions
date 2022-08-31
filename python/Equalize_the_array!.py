def equalize(arr):
    
    
    q = [x - arr[0] for x in arr]
    a = []
    for k in q : 
        if k < 0 : a.append(str(k))
        else : a.append('+' + str(k))
    return a
