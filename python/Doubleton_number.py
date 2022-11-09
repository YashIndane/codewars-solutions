from collections import Counter
def doubleton(num):
    while True:
        w = str(num+1)
        c = dict(Counter(w))
        if len(c.keys()) == 2:
            return num+1
        else:
            num+=1
