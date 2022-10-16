def str_to_hash(st): 
    # your code here
    if st=="":
        return {}
    else:
        k = {}
        w = st.split(', ')
        #print(st)
        for x in w:
            i = x.index('=')
            k[x[:i]] = int(x[i+1:])
    return k
