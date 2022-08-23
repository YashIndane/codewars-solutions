def sort_dict(d):
    
    d = dict(sorted(d.items() , key = lambda x : x[1]))
    u = []
    for k , v in d.items() : 
          u.append((k , v))
    u.reverse()
    return u
