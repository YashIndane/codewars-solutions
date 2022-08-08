from collections import Counter
def duplicate_count(text):
    text = text.lower()
    a = dict(Counter(text))
    s = [k for k , n in a.items() if n >= 2]
    return len(s)
