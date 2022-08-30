def reverse_factorial(num):
    
        p = 1
        i = 1
        while p != num : 
            p *= i
            i += 1
            if p > num :
                return 'None'
                break
        
        if i != 1 : 
          return str(i - 1) + '!'
        else : 
            return str(i) + '!'
