def highest_value(a, b):
    a_, b_ = sum([ord(x) for x in a]), sum(ord(d) for d in b)
    if a_>=b_:
        return a
    else:
        return b
