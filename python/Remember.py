def remember(str_):
    #your code here
    d = {}
    s = {}
    for i in str_:
        if i not in d:
            d[i] = 0
        else:
            if i not in s:
                s[i] = 0
    return list(s.keys())
