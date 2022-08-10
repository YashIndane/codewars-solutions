def sum_of_intervals(intervals):
    w = set()
    for x in intervals : 
      a = list(range(x[0] , x[1]))
      for c in a : w.add(c)
    return len(w
