def flatten_and_sort(array):
    w = []
    for x in array:
       w.extend(x)
    return sorted(w)
