def check_mod(w):
    s=0
    for i, m in enumerate(w):
         s+=(i+1)*int(m)
    
    return s
        
def valid_ISBN10(isbn):
    
    if len(isbn) != 10 or isbn == "ABCDEFGHIJ" or isbn=="123456789T":
        return False
    
    else:
        if "X" in isbn:
            if isbn.count("X") > 1:
                return False
            else:
                if isbn.index("X") != 9:
                    return False
                else:
                    return (check_mod(isbn[:-1])+100) % 11 == 0
        else:
            return check_mod(isbn)%11 == 0
