def sort_array(source_array):
 
    eve_idx = [k for k , i in enumerate(source_array) if i % 2 == 0]
    ods = [m for m in source_array if m % 2 == 1]
    ods.sort()
    
    li = []
    c = 0
    for i in range(len(source_array)) : 
      if i not in eve_idx : 
      
         li.append(ods[c])
         c += 1
      else : 
        li.append(source_array[i])
    return li
