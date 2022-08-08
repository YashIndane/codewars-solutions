from collections import Counter

def find_it(arr) : 
   c = dict(Counter(arr))
   a = [k for k , v in c.items() if v % 2 == 1] 
   return a[0]
