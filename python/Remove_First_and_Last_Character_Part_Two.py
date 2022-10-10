def array(string):
    s = string.split(',')
    return None if len(s) <= 2 else ' '.join(s[1:-1])
