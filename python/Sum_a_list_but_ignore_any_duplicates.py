def sum_no_duplicates(l):
    # write your solution here
    c = __import__("collections").Counter(l)
    w = 0
    for k, v in c.items():
        w += k if v==1 else 0
    return w
