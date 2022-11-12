def hidden(num):
    # Code here
    w = {"a" : 6,
        "b" : 1, 
        "d" : 7,
        "e" : 4,
        "i" : 3,
        "l" : 2,
        "m" : 9,
        "n" : 8,
        "o" : 0,
        "t" : 5}
    
    w = {a:b for b, a in w.items()}
    k = ""
    for x in str(num):
        k+=w.get(int(x))
    return k
