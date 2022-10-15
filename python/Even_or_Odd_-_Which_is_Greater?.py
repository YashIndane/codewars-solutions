def even_or_odd(s):
    # your code here
    o = sum([int(x) for x in s if int(x)%2==1])
    e = sum([int(c) for c in s])-o
    return 'Even is greater than Odd' if e>o else 'Odd is greater than Even' if o>e else 'Even and Odd are the same'
