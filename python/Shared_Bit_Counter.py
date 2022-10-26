def shared_bits(a, b):
    a=bin(a).replace('0b','')
    b=bin(b).replace('0b','')
    
    if len(a)!= len(b):
        m=a if len(a)>=len(b) else b
        n=a if len(a)<len(b) else b
    
        n='0'*(len(m)-len(n))+n
    
    else:
        m=a
        n=b
    c=0
    for i in range(len(m)):
        if m[i] == '1' and n[i] == '1':
            c+=1
        if c>=2:
            return True
    return False
