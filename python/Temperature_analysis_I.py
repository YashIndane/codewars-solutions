def lowest_temp(t):
    if len(t) == 0 : return None
    else : 
      a = t.split(' ')
      a = [int(x) for x in a]
      return min(a)
