def remove(s):
    for i in range(9999999):
        if s.endswith('!'):
            s=s[:-1]
        else:
            return s
