def peak(arr):
    for i in range(1, len(arr)-1):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
