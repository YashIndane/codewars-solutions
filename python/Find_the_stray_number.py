def stray(arr):
    return sorted(arr, key=lambda x: arr.count(x))[0]
