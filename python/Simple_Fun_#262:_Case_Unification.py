def case_unification(c):
    return c.upper() if sum([1 for x in c if x.isupper()]) > sum([1 for u in c if u.islower()]) else c.lower()
