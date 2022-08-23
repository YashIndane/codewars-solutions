def is_prime(n):
  'Return True if n is a prime number otherwise return False'
  
  if n == 0 : return False
  elif n == 1 : return False
  c = 0  
  for i in range(1 , int(n / 2) + 1) : 
        if n % i == 0 : c += 1
        if c == 2 : 
            return False
  return True
