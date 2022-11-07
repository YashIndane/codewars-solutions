def move_ten(st):
    return ''.join(chr(ord(x)+10) if ord(x)+10<=ord('z') else chr(ord(x)-16) for x in st)
