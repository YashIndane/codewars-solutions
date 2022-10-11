def two_highest(arg1):
    if not arg1:
        return []
    else:
        w = set(arg1)
        if len(w) < 2:
            return [list(w)[0]]
        else:
            q = sorted(list(w), reverse=True)
            return [q[0], q[1]]
