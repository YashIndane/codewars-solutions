def add(num1, num2):
    a,b=str(num1),str(num2)
    if len(str(num1))==len(str(num2)):
        d=''
        for i in range(len(a)):
            d+=str(int(a[i])+int(b[i]))
        return int(d) 
    else:
        d=''
        ma= str(a) if len(str(a))>len(str(b)) else str(b)
        mi= str(a) if len(str(a))<len(str(b)) else str(b)
        mi= '0'*(len(ma)-len(mi))+mi
        for i in range(len(mi)):
            d+=str(int(mi[i])+int(ma[i]))
        return int(d)
