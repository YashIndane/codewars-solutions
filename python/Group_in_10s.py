def group_in_10s(*args):
    l = []
    if args:
        for v in range(0, max(args)//10+1):
            s = list(filter(lambda x: (v == x//10) or (v == 0 and x//10==0), args))
            l.append(sorted(s) if s else None)
        return l
    else:
        return []
