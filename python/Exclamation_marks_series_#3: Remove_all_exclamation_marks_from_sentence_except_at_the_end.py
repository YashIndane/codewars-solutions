def remove(s):
    u = ""
    flag = False
    l = len(s)
    for i in range(1, len(s)+1):
        if s[l-i] != '!':
            flag = True
        if not flag:
            u += s[l-i]
        else:
            if s[l-i] != '!':
                u += s[l-i]
    return u[::-1]
