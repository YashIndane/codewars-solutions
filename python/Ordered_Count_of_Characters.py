def ordered_count(inp):
    w = []
    for x in dict(__import__("collections").Counter(inp)).items():
        w.append((x[0], x[1]))
    return w
