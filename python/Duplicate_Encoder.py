from collections import Counter
def duplicate_encode(word):
    #your code here
    word = word.lower()
    w = dict(Counter(word))
    v = ""
    for x in word:
        if w.get(x) == 1:
            v += "("
        else:
            v += ")"
    return v
