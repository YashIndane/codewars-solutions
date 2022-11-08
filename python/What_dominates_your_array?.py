def dominator(arr):
    #your code here
    

    half = len(arr)//2
    for x in arr:
        if arr.count(x) > half:
            return x
    return -1
