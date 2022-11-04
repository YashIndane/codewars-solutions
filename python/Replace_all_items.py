def replace_all(obj, find, replace):
    if isinstance(obj, str):
        w=''
        for x in obj:
            w+= x if x!=find else replace
        return w
    else:
        e=[]
        for x in obj:
            e.append(x if x!=find else replace)
        return e
