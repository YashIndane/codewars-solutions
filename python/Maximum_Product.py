def adjacent_element_product(array):
    w = -99999999999
    for i in range(len(array)-1):
        w = max(w, array[i]*array[i+1])
    return w
