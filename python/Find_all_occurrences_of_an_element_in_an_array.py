def find_all(array, n):
    # your code here
    e = []
    for i, v in enumerate(array):
        if v==n:
            e.append(i)
    return e
