def count_salutes(hallway):
    # Your code goes here :)
    l = 0
    w = 0
    for x in hallway:
        if x == '<':
            w += l*2
        if x == '>':
            l += 1
            
    return w
