from collections import Counter
def letter_count(s):
    q = dict(Counter(s))
    
    q = dict(sorted(q.items() , key = lambda x : x[0]))
    return q
