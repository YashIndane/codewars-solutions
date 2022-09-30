def solve(arr): 
    w = []
    for x in range(len(arr)):
        if arr[~x] not in w:
            w.insert(0, arr[~x])
    return w
