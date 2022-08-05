def find_even_index(arr):
    c = 0
    for i in range(len(arr)) : 
        if i == 0 : 
          if sum(arr[i + 1 :]) == 0 : 
             return 0
             break
        elif i > 0 : 
            if sum(arr[:i]) == sum(arr[i+1:]) : 
              return i
              break
        elif i == len(arr) - 1 :
            if sum(arr[: i]) == 0 : 
              return i
              break
        c += 1
        if c == len(arr): return -1
