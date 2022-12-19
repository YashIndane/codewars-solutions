from itertools import filterfalse
def reject(seq, predicate): 
    # your code here
    return list(filterfalse(predicate, seq))
