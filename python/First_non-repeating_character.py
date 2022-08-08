from itertools import groupby
def first_non_repeating_letter(string):
     z = string.lower()
     a = []
     if z == '' : return ''
     
     else : 
      c = 0
      for x in z : 
        if z.count(x) == 1 : 
           return x.upper() if string[c].isupper() else x
           break
        c += 1
      if c == len(z) : return ''
