def get_number_of_squares(n):
    
    x = 0
    s = 0
    while s < n : 
        x += 1
        s += x ** 2
    return x - 1
