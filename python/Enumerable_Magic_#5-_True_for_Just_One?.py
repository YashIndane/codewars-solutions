def one(sq, fun): 
    # your code here
    w = [fun(x) for x in sq]
    return w.count(True) == 1
