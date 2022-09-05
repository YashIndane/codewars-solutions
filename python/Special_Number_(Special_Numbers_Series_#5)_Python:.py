def special_number(number):
    return 'Special!!' if all([int(x) in [0,1,2,3,4,5] for x in str(number)]) else 'NOT!!'
