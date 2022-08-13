from functools import reduce
def factorial(n):
   
   return int(reduce(lambda x , v : x * v , list(range(1 , n + 1 )))) if n != 0 else 1
