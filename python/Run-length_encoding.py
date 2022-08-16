from itertools import groupby
def run_length_encoding(s):
    z = groupby(s)
    b = []
    for a , n in z :
       temp = []
       temp.append(len(list(n)))
       temp.append(a)
       b.append(temp)
    return b
