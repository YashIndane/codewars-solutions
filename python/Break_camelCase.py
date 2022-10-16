def solution(s):
    q = ''
    for x in s:
        if x.islower():
            q += x
        else:
            q += ' ' + x
    return q
