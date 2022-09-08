import collections
def freq_seq(s, sep):
    w = dict(collections.Counter(s))
    q = ""
    for k in s:
        q += str(w.get(k)) + sep
    return q[:len(q)-1]
