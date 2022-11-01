def averages(arr):
    if arr==None or len(arr)<=1:
        return []
    else:
        w=[]
        for x in range(len(arr)-1):
            w.append((arr[x]+arr[x+1])/2)
    return w
