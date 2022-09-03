def incrementer(nums) : 
    
    x = []
    for i , c in enumerate(nums) : 
        x.append(int(str(c + i + 1)[-1]))
    return x
