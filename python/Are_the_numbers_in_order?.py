def in_asc_order(arr):
    # random_ is not allowed
    if len(arr) <= 1:
        return True
    else:
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
        return True
