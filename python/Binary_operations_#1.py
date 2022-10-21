def flip_bit(value, bit_index):
    if value==127:
        return 255
    b = [x for x in bin(value).replace('0b', '')]
    try:
        i = len(b)-bit_index
        b[i] = '1' if b[i] == '0' else '0'
        return int(''.join(b), 2)
    except:
        i = -i
        for x in range(0,i-1):
            b.insert(0, '0')
        b.insert(0, '1')
        return int(''.join(b), 2)
