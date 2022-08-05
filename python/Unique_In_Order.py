from itertools import groupby

def unique_in_order(x):
   q = groupby(x)
   temp  =  []
   
   for x ,v in q : 
      temp.append(x)
    
   return temp
