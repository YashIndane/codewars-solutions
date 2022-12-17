def repeats(arr):
    return sum(list(filter(lambda x: arr.count(x)==1, arr)))
