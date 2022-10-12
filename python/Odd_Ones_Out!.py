def odd_ones_out(numbers):
    return list(filter(lambda x: numbers.count(x)%2 == 0, numbers))
