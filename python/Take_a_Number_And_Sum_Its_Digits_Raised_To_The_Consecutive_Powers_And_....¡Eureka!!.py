def fun(x):
    return sum([int(v)**(i+1) for i, v in enumerate(x)]) == int(x)
    

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    l=[]
    for i in range(a, b+1):
        m=fun(str(i))
        if m:
            l.append(i)
    return l
