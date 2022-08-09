def to_camel_case(text):
   flag1 = False
   q = ''
   for  x in text : 
      if x in ['-' , '_'] : 
        flag1 = True
        continue
        
      if flag1 :
        q += x.upper()
        flag1 = False
      else : 
        q += x
   return q
