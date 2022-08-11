def find_outlier(integers):
    eve = [x for x in integers if abs(x) % 2 == 0]
    odd = [y for y in integers if abs(y) % 2 == 1]
    return eve[0] if len(eve) == 1 else odd[0]
