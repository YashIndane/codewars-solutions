def camelize(str_):
    #your code here
    a="0123456789abcdefghijklmnopqrstuvwxyz"
    a=a+a.upper()
    q=""
    s=""
    for x in str_:
            if x in a:
                s+=x
            else:
                s=s.lower().capitalize()
                q+=s
                s="" 
                
    return q+s.lower().capitalize()
