def find_in_array(seq, predicate): 
    # your code here
    for i, v in enumerate(seq):
        if predicate(v, i):
            return i
    return -1
