from itertools import permutations
def permutation_average(n) : 
    n = str(n)
    w = list(permutations(n , len(n)))
    q = [int(''.join(list(c))) for c in w]
    return round(sum(q) / len(q))
