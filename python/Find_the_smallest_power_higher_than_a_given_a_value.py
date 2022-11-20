import math
def find_next_power(val, pow_):
    #your code here
    n = val**(1/pow_)
    if "." in str(n):
        return math.ceil(n)**pow_
    else:
        return (n+1)**pow_
