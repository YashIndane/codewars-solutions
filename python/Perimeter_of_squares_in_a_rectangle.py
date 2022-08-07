def perimeter(n):
    a , b = 1 , 1
    
    arr = []
    
    arr.append(a)
    arr.append(b)
    while len(arr) < n + 1 : 
       u = b
       v = a
       a = b
       b = v + u
       arr.append(b)
    return 4 * sum(arr)
