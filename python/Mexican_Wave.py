def wave(people):
    # Code here
    w = []
    for i in range(0, len(people)):
        if people[i] != ' ':
            w.append(people[0:i]+people[i].upper()+people[i+1:])
    return w
