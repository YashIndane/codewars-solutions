from collections import Counter
def count_consonants(text):
    # Your code here:
    text = text.lower()
    v = 'BCDFGHJKLMNPQRSTVWXYZ'.lower()
    q = dict(Counter(text))
    w = [x for x in q.keys() if x in v]
    return len(w)
