def jumping_number(number):
    w = str(number)
    for i in range(len(w) - 1) : 
        if abs(int(w[i]) - int(w[i + 1])) != 1 :
               return 'Not!!'
    return 'Jumping!!'
