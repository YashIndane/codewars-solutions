def remove(s):
    if s:
        return s[:-1] if s[-1] == "!" else s
    else:
        return ''
