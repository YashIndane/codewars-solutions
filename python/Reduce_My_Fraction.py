from math import gcd
def reduce_fraction(fraction):
    g = gcd(fraction[0] , fraction[1])
    
    return (int((fraction[0]) / g) , int(fraction[1] / g))
