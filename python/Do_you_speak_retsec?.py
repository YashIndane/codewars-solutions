def reverse_by_center(s):
    if len(s) % 2 == 0 : 
        x = int((len(s) / 2) - 1)
        return s[x + 1 : ] + s[: x + 1]
    else : 
        x = int(len(s) / 2)
        return s[x + 1 :] + s[x] + s[ : x]
