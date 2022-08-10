def differentiate(e, p):
    
      w = []
      temp = ''
      e += '+'
      flag = False
      
      for n in e if e[0] not in ['+' , '-'] else e[1 : ] : 
           
             if n != ' ' :
                 if n not in ['+' , '-'] : temp += n
                 
                 else : 
                    if 'x' in temp : 
                      if flag : 
                          w.append('-' + temp)
                      else : w.append(temp)
                    flag =  n == '-' 
                    
                    temp  = ''
      if e[0] ==  '-' : w[0] = '-' + w[0]
      
      s = 0
      
      for terms in w : 
          if '^' in terms : 
              if '-' in terms : 
                  power = int(terms[terms.index('^') + 1 : ])
                  if terms.index('x') - terms.index('-') > 1 : 
                       power = int(terms[terms.index('^') + 1 : ])
                       m = -int(terms[1 : terms.index('x')]) * power * (p ** (power - 1))
                  else : 
                       m = -1  * power * (p ** (power - 1))
              else : 
                    power = int(terms[terms.index('^') + 1 :])
                    if terms.index('x') > 0 : 
                       m = int(terms[0 : terms.index('x')]) * power * (p ** (power -1))
                    else :
                       m = 1 * power * (p ** (power - 1))
                       
          else  : 
              if '-' in terms : 
                  if terms.index('x') - terms.index('-') > 1 :
                  
                     m = -int(terms[1 : terms.index('x')])
                  else : 
                     m = -1 
              else : 
                   if terms.index('x') > 0 : 
                     m = int(terms[0 : terms.index('x')])
                     
                   else : 
                      m = 1
                      
          s += m   
          
      return s
