def divisions(n, divisor):
    
    i = 0
    while n >= divisor ** i :  i += 1
    return i - 1
