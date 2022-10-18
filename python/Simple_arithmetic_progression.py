from itertools import combinations
def solve(arr):
    w = [sorted(k) for k in set(combinations(arr, 3))]    
    return len([x for x in w if x[1]-x[0] == x[2]-x[1]])
