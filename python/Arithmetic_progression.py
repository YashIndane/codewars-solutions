def arithmetic_sequence_elements(a, d, n):
    #Your code here!:)
    w = ""
    e = 0
    for x in range(n):
        e = e + a
        w += str(e) + ", "
        a = d
    return w[:-2]
