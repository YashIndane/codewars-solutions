import math

def fun(x):
    return True if all([int(c)%2 == 0 for c in str(x**2)]) else False
    

def even_digit_squares(a, b):
    # your code here
    return [x ** 2 for x in list(filter(fun, range(math.ceil(a**0.5), int(b**0.5)+1)))]
