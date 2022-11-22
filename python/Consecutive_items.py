def consecutive(arr, a, b):
    # Do some magic
    for i in range(len(arr)-1):
        if arr[i:i+2] == [a, b] or arr[i:i+2] == [b, a]:
            return True
    return False
