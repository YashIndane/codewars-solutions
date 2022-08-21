def reverse_letter(string):
    q = [x for x in string if x.isalpha()]
    a = ''.join(q)
    a = a[::-1]
    return a
