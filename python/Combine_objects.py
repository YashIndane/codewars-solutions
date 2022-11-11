from collections import defaultdict
def combine(*args):
    #your code here
    d = defaultdict(int)
    for obj in args:
        for i, j in obj.items():
            d[i] += j
    return d
