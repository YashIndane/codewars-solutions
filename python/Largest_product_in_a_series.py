from functools import reduce
def greatest_product(n):
    a = 0
    for i in range(0 , len(n) - 4) : 
      p = int(reduce(lambda v , x : int(v) * int(x) , n[i : i + 5]))
      if p > a : a = p
    return a
