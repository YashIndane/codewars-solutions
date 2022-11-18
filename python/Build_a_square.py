def generate_shape(n):
    q = ""
    for x in range(n):
        q += "+"*n + "\n"
        
    return q[:-1]
