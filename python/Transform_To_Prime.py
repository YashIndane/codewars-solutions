def minimum_number(numbers):
    
    def isprime(x):
        c = 0
        for i in range(1 , int(x / 2)) :
            if x % i == 0 : c += 1
            if c == 2 : return False     
        return True    
        
    
    s = sum(numbers)
    x = s
    if isprime(s) : return 0
    
    else : 
         while True : 
                s += 1
                if isprime(s) : return s - x
