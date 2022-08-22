def binary_to_string(binary):
    x = binary.split('0b')
    x = x[1:]
    w = ''
    for v in x : 
        w += chr(int(v , 2))
    return w
