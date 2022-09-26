def correct(s):
    w = ''
    for x in s:
        if x == '0':
            w += 'O'
        elif x == '5':
            w += 'S'
        elif x == '1':
            w += 'I'
        else:
            w += x
    return w
