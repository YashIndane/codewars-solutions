def tidyNumber(n):
    j = str(n)
    for x in range(len(j) - 1) : 
        if int(j[x]) > int(j[x + 1]) :
           return False
    return True
