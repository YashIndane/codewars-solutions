def filter_string(string):
    d = ''
    for x in string : 
         if x.isnumeric() :   d += x
    return int(d)
