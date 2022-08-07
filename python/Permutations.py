from itertools import permutations as per
def permutations(string):
    s = set()
    for perm in per(string) : 
        y = ''.join(perm)
        s.add(y)
    return [x for x in s ]
