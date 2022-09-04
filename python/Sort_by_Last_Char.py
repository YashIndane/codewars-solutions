def last(x):
    w = x.split(' ')
    w = sorted(w , key = lambda x : x[-1])
    return w
