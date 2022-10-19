def is_narcissistic(i):
    return sum([x**len(str(i)) for x in map(int, str(i))]) == i
