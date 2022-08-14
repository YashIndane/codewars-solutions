def swap(string_):
    a = ''
    for k in string_ : 
       a += k.lower() if k.isupper() else k.upper()
    return a
