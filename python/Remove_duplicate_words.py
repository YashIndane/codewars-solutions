def remove_duplicate_words(s):
    w = s.split(" ")
    q = ""
    for x in w:
        if x not in q:
            q += x + " "
    return q[:-1]
