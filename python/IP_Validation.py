def is_valid_IP(strng):
    a="0123456789"
    if strng.count(".") == 3:
        w=strng.split(".")
        k=[]
        for x in w:
            if x.startswith("0") and len(x)>1:
                return False
            else:
                xx=all([j in a for j in x])
                if xx:
                    try:
                        k.append(0<=int(x)<=255)
                    except:
                        return False
                        
                else:
                    return False
        return all(k)
    else:
        return False
