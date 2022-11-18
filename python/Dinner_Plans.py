def common_ground(s1,s2):
    #your code here
    s = ""
    w = s1.split(" ")
    for x in s2.split(" "):
        if x in w and x not in s.split(" "):
            s += x + " "
    return s[:-1] if len(s[:-1]) > 0 else "death" 
