from collections import defaultdict
def count_languages(lst): 
    # your code here
    d = defaultdict(int)
    for x in lst:
        d[x["language"]] += 1
    return dict(d)
