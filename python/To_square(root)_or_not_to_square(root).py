def fun(x):
    s = x**0.5
    if s%1 == 0:
        return round(s)
    else:
        return x**2

def square_or_square_root(arr):
    return list(map(fun, arr))
