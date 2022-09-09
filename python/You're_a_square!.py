def is_square(n):    
    if n < 0:
        return False
    elif n == 0:
        return True
    else:
        q = n**0.5
        j = str(q)
        ind = j.index(".")
        e = float("0" + j[ind:])
        if e > 0:
            return False
        else:
            return True
