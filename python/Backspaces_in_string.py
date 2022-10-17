def clean_string(s):
    # your code here
    if s.count('#') == len(s) or s == "":
        return ""
    else:
        w = ''
        for c in s:
            if c != '#':
                w += c
            else:
                w = w[:-1]
    return w
