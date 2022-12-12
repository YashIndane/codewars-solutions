def triple_x(s):
    if s.count('x')>2:
        i=s.index("x")
        if s[i+1: i+3] == "xx":
            return True
        else:
            return False
    else:
        return False
