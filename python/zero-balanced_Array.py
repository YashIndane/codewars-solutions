def is_zero_balanced(arr):
    #your code here
    if len(arr)>1:
        s=sum(arr)
        t=False
        for x in arr:
            if -x not in arr:
                return t
        return True and s==0
                
            
        
    else:
        if arr==[0]: return True
        return False
