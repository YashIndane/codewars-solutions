def is_nice(arr):
    if not arr:
        return False
    return all([x+1 in arr or x-1 in arr for x in arr])
