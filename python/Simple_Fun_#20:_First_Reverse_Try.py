def first_reverse_try(arr):
    
   try : 
    a = arr[0]
    b = arr[len(arr) - 1]
    arr[0] = b
    arr[len(arr) - 1] = a
    return arr
   except : 
        return []
