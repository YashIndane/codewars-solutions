def multiple(x):
    if x%15!=0:
        if x%3 == 0:
            return 'Bang'
        if x%5 == 0:
            return 'Boom'
        return 'Miss'
    else:
        return 'BangBoom'
