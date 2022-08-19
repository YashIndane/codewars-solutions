from itertools import groupby
def ones_counter(input):
    z = groupby(input)
    w = []
    
    for x , y in z : 
         if x == 1 :  
                w.append(len(list(y)))
    return  w
