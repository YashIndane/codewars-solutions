def solve(st):
    
        if len(st) == 1:
            return 0
    
    
        i = (len(st)-1)//2 if len(st) % 2 == 1 else len(st)//2
        j = 0
        for c in range(0, i):
            if st.endswith(st[0:c+1]):
                j = c+1
            
        return j
