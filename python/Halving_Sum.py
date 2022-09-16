def halving_sum(n): 
    # your code here
    w = n
    while n>1:
        n //= 2
        w += n
    return w
