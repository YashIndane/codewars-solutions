def eliminate_unset_bits(number):
    w = number.replace('0', '')
    return int(w, 2) if w else 0
