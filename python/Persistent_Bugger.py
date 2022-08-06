from functools import reduce
def persistence(n):
    str_ =  str(n)
    counter = 0
    while len(str_) != 1 :
       str_ = str((reduce(lambda x, v : int(x) * int(v) , str_)))
       counter += 1
    return counter
