def string_breakers(n, st): 
    # your code here
    st = st.replace(' ', '')
    c=0
    q=[]
    temp=''
    for k in st:
        
        if c == n:
            c = 0
            q.append(temp)
            temp = k
        else:
            temp += k
            
            
        c += 1 
    try:    
        if temp != q[-1]: 
            q.append(temp)
    except:
        q.append(temp)
        
        
    #print(q)    
    return '\n'.join(q)
