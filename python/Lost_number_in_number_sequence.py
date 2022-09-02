def find_deleted_number(arr, mixed_arr):
    a = set(arr)
    b = set(mixed_arr)
    try : 
      return [z for z in a.difference(b)][0]
    except : 
        return 0
