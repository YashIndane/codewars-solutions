from itertools import groupby
def valid_spacing(s):
    # write your code here
    if any([s.startswith(' '), s.endswith(' ')]):
        return False
    else:
        w = groupby(s)
        for a, b in w:
            if a == ' ' and len(list(b)) >1:
                return False
            
        return True
