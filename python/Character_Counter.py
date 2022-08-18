from collections import Counter
def validate_word(word):
    
    word = word.lower()
    a = dict(Counter(word))
    q = list(a.values())
    s = q[0]
    return all([s == x for x in q])
