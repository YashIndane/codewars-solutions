def factors(x):
    try : 
     if x < 1 : return -1
     w = [c for c in list(range(1 , x + 1)) if x % c == 0]
     w.reverse()  
     return w
    except : return -1
