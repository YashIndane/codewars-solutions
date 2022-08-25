def consecutive(arr):
    if len(arr) >= 2 :
        w = set(list(range(min(arr) , max(arr) + 1)))
        arr = set(arr)
        q = w.difference(arr)
        return len(q)
    else : 
        return 0
