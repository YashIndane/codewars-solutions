def in_array(array1, array2):
    # your code
    w = []
    for x in array1:
        for y in array2:
            if x in y:
                w.append(x)
    return sorted(set(w))
