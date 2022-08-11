import heapq
def max_product(a):
   q = list(heapq.nlargest(2 , a))
   return q[0] * q[1]
