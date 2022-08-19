from functools import reduce
def product(numbers):
    
    try : 
      return int(reduce(lambda x , v : x * v , numbers))
    except : 
        return None
