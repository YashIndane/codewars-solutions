def count_vowels(s = ''):
     
       c = 0
       try : 
         s = s.lower()
       except :  return None 
       for x in s : 
         if x in ['a' , 'e' , 'i' , 'o' , 'u'] :
           c += 1
       return c
