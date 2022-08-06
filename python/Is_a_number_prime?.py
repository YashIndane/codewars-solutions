def is_prime(num):
    if num <= 1 : return False
    else : 
      threashold = int(num ** 0.5)
      for i in range(2 , threashold + 1) :
        if num % i == 0 :
           return False
           break
      return True
