def to_jaden_case(string):
    w=''
    for x in string.split():
        w+=x.capitalize() + ' '
    return  w[:-1]
