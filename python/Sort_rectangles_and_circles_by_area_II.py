def area(x):
    if isinstance(x, (float, int)):
        return 3.14*(x**2)
    else:
        return x[0]*x[1]

def sort_by_area(seq): 
    return sorted(seq, key=area)
