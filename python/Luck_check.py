def luck_check(string):
    q="0123456789"
    s=[x for x in string]
    inv=all([x in q for x in s])
    if inv:
        if len(string)%2==0:
            m=len(string)//2
            a=string[0:m]
            b=string[m:]
            #print(string)
            return sum(map(int, a))==sum(map(int, b))
        else:
            m=len(string)//2
            a=string[0:m]
            b=string[m+1:]
            return sum(map(int, a))==sum(map(int, b))
    else:
        raise Exception("invalid")
