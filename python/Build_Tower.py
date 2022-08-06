def tower_builder(n_floors):
    t = '*'*(int(n_floors * 2 - 1))
    s = list('*'*(int(n_floors * 2 - 1)))
    temp = []
    a = 0
    fin = []
    fin.append(t)
    for i in range(n_floors - 1) : 
       s[a] = ' '
       s[len(s) - 1 - a] = ' '
       a += 1
       fin.append(''.join(s))
       
    fin.reverse()  
    return fin
