def solution(number):
  l5_3 = set()
  for k in range(number) : 
     
     l5_3.add(k if any([k % 3 == 0 , k % 5 == 0]) else 0)
  return sum(l5_3) 
