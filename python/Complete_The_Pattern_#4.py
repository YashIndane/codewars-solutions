def pattern(n):
  
    z = ''
    for i in range(n) : 
        z += ''.join([str(v) for v in list(range(i + 1 , n + 1))]) + '\n'
    return z[:len(z) - 1]
