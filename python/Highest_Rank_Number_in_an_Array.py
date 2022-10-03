def highest_rank(arr):
    # your code here
    w = max([arr.count(x) for x in arr])
    return max([x for x in arr if arr.count(x) == w])
