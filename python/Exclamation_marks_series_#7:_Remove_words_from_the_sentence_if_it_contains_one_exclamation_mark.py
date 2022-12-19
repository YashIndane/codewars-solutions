def remove(s):
    s=s.split()
    return " ".join(list(filter(lambda z:z.count("!")>1 or z.count("!")==0, s)))
