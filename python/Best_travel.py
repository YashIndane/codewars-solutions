from itertools import combinations
def choose_best_sum(t, k, ls):
    
    all_combis = list(combinations(ls , k))
    all_sums = [sum(x) for x in all_combis]
    
    all_sums = sorted(all_sums , reverse = True)
    for k in all_sums : 
      if t >= k : 
        return k
        break
