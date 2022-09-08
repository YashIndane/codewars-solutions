import collections
def solve(st):
    if len(st) == 1:
        return True
    q = "abcdefghijklmnopqrstuvwxyz"
    s = [x for x in st]
    p = set(s)
    if len(s) != len(p):
        return False
    else:
        s.sort()
        a = "".join(s)
        return a in q
