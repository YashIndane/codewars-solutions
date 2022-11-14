def create_phone_number(n):
    c1 = ''.join(list(map(str, n[0:3])))
    c2 = ''.join(list(map(str, n[3:6])))
    c3 = ''.join(list(map(str, n[6:])))
    return '('+c1+') ' + c2 + '-'+c3
