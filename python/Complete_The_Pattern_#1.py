def pattern(n):
    s = ''
    for i in range(1 , n + 1) :  s += str(i) * i + '\n'
    return s[:len(s) - 1
