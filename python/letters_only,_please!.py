def remove_chars(s):
    return ''.join(list(filter(lambda x: x.isalpha() or x==" ", s)))
