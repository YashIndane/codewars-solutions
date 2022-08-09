def max_sequence(arr):
      v = []
    #if all([h < 0 for h in arr]) or len(arr) == 0 :return 0
    #elif all([k > 0 for k in arr]):return sum(arr)
    #else : 
      if all([h < 0 for h  in arr]) : 
          return 0
      for i in range(len(arr)) : 
        for j in range(i + 1 , len(arr)) : 
           v.append(sum(arr[i : j + 1]))
      try :      
         return max(v)
      except : return 0
