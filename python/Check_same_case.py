def same_case(a, b): 
    # your code here
    z = "abcdefghijklmnopqrstuvwxyz"
    y = z.upper()
    if (a not in z and a not in y) or (b not in z and b not in y):
        return -1
    if (a in z and b in z) or (b in y and a in y):
        return 1
    else:
        return 0
