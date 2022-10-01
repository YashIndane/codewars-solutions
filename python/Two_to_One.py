def longest(a1, a2):
    return ''.join(sorted(set([x for x in a1+a2])))
