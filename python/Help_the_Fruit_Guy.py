def remove_rotten(array):
    if array:
        w = []
        for f in array:
            if "rotten" in f:
                w.append(f[6:].lower())
            else:
                w.append(f)
        return w        
    else:
        return []
