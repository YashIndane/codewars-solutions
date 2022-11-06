from collections import defaultdict
def count_duplicates(name,age,height):
    # your code here
    d = defaultdict(int)
    q = list(zip(name, age, height))
    for x in q:
        d[x] += 1
    return sum([x-1 for x in d.values() if x>1])
