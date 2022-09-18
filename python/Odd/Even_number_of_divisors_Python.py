def oddity(n):
    if n == 1:
        return 'odd'
    w = int(n**0.5)
    k = {}
    j = 0
    for i in range(2, w+1):
        if n%i == 0 and i not in k:
            j += 1
            k[i] = 0
            if n//i not in k:
                j += 1
                k[n//i] = 0
                
    return 'odd' if j%2 != 0 else 'even'
