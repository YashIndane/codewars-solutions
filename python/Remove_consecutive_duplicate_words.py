from itertools import groupby
def remove_consecutive_duplicates(s):
    k = ''
    s = s.split()
    for x, n in groupby(s):
        k += x+' '
    return k[:-1]
