def is_vow(inp):
    d={97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}
    return [x if x not in d else d[x] for x in inp]
