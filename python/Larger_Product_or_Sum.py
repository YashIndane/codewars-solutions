import math
def sum_or_product(array, n):
    return [["sum", "product"][int(sum(sorted(array)[-n:]) < math.prod(sorted(array)[:n]))], "same"][int(sum(sorted(array)[-n:]) - math.prod(sorted(array)[:n]) == 0)]
