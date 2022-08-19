from functools import reduce
def max_product(lst, n_largest_elements):
    lst = sorted(lst , reverse = True)
    return int(reduce(lambda x , y : x * y , lst[:n_largest_elements]))
