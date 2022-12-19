def capitalize(s,ind):
    for i in ind:
        if i<len(s):
            s=s[:i]+s[i].upper()+s[i+1:]
    return s
