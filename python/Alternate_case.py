def alternateCase(s):
    
    k = ''
    for n in s : k += n.lower() if n.isupper() else n.upper()
    return k
