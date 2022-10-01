def calc(x):
    # your code here
    a = ''.join([str(ord(c)) for c in x])
    b = a.replace('7', '1')
    
    a = sum([int(v) for v in a])
    b = sum([int(s) for s in b])
    
    return a-b
