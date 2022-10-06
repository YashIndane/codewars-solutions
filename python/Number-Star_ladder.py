def pattern(n):
    e = ''
    for x in range(n):
        if x != 0:
            e += '1' + '*'*x + str(x+1)+'\n'
        else:
            e += '1\n'
    return e[:-1]
