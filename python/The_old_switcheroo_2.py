def encode(string):
    #your code here
    q = "abcdefghijklmnopqrstuvwxyz"
    w = ""
    string = string.lower()
    for x in string:
        if x in q:
            w += "{}".format(q.index(x)+1)
        else:
            w += x
    return w
