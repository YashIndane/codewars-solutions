def solve(a):
    q = list(filter(lambda x: isinstance(x, int), a))
    e = len([x for x in q if x%2==0])
    o = len([x for x in q if x%2==1])
    return e-o
