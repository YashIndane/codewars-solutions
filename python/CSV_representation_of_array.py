def to_csv_text(array):
    w = ""
    for x in array:
        w += ",".join(list(map(str, x))) + "\n"
    return w[:-1]
