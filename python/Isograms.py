from collections import Counter
def is_isogram(string):
    #your code here
    for x in dict(Counter(string.lower())).values():
        if x > 1:
            return False
    return True
