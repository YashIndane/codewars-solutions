def spoonerize(words):
    # ...aaaaand SPOONERIZE!
    w = words.split()
    a, b = w
    t = a[0]
    a = b[0] + a[1:]
    b = t + b[1:]
    return a +' '+ b
