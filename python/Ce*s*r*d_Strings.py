def uncensor(infected, discovered):
    d=0
    if discovered:
        for i in range(len(infected)):
            if infected[i] == "*":
                infected = infected[:i] + discovered[d] + infected[i+1:]
                d+=1
        return infected    
    else:
        return infected
