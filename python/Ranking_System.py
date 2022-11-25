def rankings(arr):
    return [sorted(arr, reverse=True).index(x)+1 for x in arr]
