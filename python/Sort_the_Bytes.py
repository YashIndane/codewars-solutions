def sort_bytes(number):
    # your code
    b=bin(number)[2:]
    b="0"*(32-len(b))+b
    a,b,c,d=b[0:8], b[8:16],b[16:24],b[24:32]
    return int("".join(sorted([a,b,c,d], key=lambda x: int(x, 2), reverse=True)), 2)
