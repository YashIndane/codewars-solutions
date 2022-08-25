from functools import reduce
def string_color(name):
    
    if len(name) >= 2 : 
         l = [ord(x) for x in name]
            
         s = sum(l) % 256
         p = int(reduce(lambda x , v : x * v , l)) % 256
         d = abs(l[0] - sum(l[1:])) % 256
        
         v = [hex(b)[2:].upper() for b in [s , p , d]]
         z = ''   
         for j in v :
                if len(j) == 2:
                  z += j
                else : 
                  z += '0' + j  
                
         return z
    else :
         return None
