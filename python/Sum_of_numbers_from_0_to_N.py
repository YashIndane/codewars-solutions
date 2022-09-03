def show_sequence(n):
    
    if n > 0 : 
     a = ''
     w = 0
     for x in range(0 , n + 1) : 
        
        w += x
        a += str(x) + '+'
        
     return a[:len(a) - 1] + ' = ' + str(w)
     
    elif n == 0 : return "0=0"
    else : return str(n) + '<' + '0'
