def merge_arrays(arr1, arr2):
    arr1.extend(arr2)
    return sorted(list(set(arr1)))
