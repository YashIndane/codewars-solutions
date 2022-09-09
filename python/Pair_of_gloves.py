import collections
def number_of_pairs(gloves):
    #your code here
    c = dict(collections.Counter(gloves))
    w = 0
    for x in c.values():
        w += int(x/2)
    return w
