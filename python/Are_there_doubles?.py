from itertools import groupby
def double_check(strng):
    strng = strng.lower()
    a = groupby(strng)
    for k , v in a : 
         if len(list(v)) >= 2 : return True
    return False
