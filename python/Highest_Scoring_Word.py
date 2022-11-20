def score(x):
    return sum([ord(z)-96 for z in x])

def high(x):
    # Code here
    w = 0
    a = ""
    for word in x.split(" "):
        sc = score(word)
        if sc > w:
            a = word
            w = sc
    return a
