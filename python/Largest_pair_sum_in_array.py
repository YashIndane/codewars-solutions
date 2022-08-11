from itertools import combinations
def largest_pair_sum(numbers): 
      c = list(combinations(numbers , 2))
      h = list(sorted(c , key = lambda v : v[0] + v[1] , reverse = True))
      return sum([h[0][0] , h[0][1]])
