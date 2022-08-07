from collections import Counter
def scramble(s1, s2):
   s2c = dict(Counter(s2))
   return all([s1.count(key) >= count for key , count in s2c.items()])
