def swap(st):
    
    vow = 'aeiouAEIOU'
    
    a = ''
    for x in st : 
        a += x.upper() if x in vow else x
    return  a
