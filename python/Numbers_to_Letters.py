def switcher(arr):
    
    #your code here
    q = " ?!abcdefghijklmnopqrstuvwxyz,"
    q = q[::-1]
    s = ""
    for z in arr:
        s += q[int(z)]
    return s
