def reverse_slice(s):
    a = s[::-1]
    z = []
    z.append(a)
    while len(a) > 1 : 
       a = a[1:]
       z.append(a)
    return z
