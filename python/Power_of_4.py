def powerof4(n):
    if isinstance(n, int) and (str(n) != "False" and str(n)!="True"):
        print(n)
        for x in range(0, 10000):
            if n == 4**x:
                return True
        return False    
    else:
        return False
