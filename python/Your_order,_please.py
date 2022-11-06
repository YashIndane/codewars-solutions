def order(sentence):
  # code here
    w = [1,2,3,4,5,6,7,8,9]
    d = {}
    for x in sentence.split():
        for c in w:
            if str(c) in x:
                d[c] = x
    w = dict(sorted(d.items(), key=lambda x: x[0]))    
    return ' '.join(w.values())
