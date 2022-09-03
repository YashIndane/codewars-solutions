def count_balls(n):
    
    i = 1
    a = 2
    x = []
    for v in range(2 , n + 1) :
        
        i += a
        x.append(i)
        a += 1
        
    return sum(x)  + 1
