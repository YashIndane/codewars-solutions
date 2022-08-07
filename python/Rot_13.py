def rot13(message):
   s = 'abcdefghijklmnopqrstuvwxyz'
   sl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   fin = ''
   for letter in message : 
     
    try:
     if letter.islower() : 
       a = s.index(letter) + 13
       if a < len(s) - 1 : fin += s[a]
       else : fin += s[s.index(letter) - 13]
     else : 
        a = sl.index(letter) + 13
        if a < len(sl) - 1 : fin += sl[a]
        else : fin += sl[sl.index(letter) - 13]
    except : fin += letter   
   return fin
