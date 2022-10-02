def find_uniq(arr):
    # your code here
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
