def fil(x):
    q=bin(ord(x))[2:]
    return q.count("0")>q.count("1")

def more_zeros(s):
    z=[]
    for k in s:
        if fil(k) and k not in z:
            z.append(k)
    return z
