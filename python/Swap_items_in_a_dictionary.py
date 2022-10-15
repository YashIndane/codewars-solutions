from collections import defaultdict
def switch_dict(dic):
    # Your code here:
    d = defaultdict(list)
    for x, y in dic.items():
        d[y].append(x)
    return d
