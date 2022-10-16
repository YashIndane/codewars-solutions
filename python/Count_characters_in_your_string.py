from collections import Counter
def count(string):
    # The function code should be here
    return dict(Counter(string)) if string else {}
