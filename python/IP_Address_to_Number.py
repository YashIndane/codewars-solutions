def ip_to_num(ip):
    nums=list(map(int, ip.split(".")))
    w=""
    for x in nums:
        b=bin(x)[2:]
        b="0"*(8-len(b))+b
        w+=b
    return int(w, 2)
        
    
def num_to_ip(num):
    b=bin(num)[2:]
    b="0"*(32-len(b))+b
    print(b)
    a,b,c,d=int(b[:8],2), int(b[8:16],2), int(b[16:24],2), int(b[24:32],2)
    return str(a)+"."+str(b)+"."+str(c)+"."+str(d)
