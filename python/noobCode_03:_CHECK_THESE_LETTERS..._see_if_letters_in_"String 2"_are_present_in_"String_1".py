def letter_check(arr): 
    arr[0] = arr[0].lower()
    arr[1] = arr[1].lower()
    
    return all([x in arr[0] for x in arr[1]])
