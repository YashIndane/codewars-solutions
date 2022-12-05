def find_2nd_largest(arr):
    # your code here
    a = list(filter(lambda x : isinstance(x, int), arr))
    a = sorted(set(a))
    return a[-2] if len(a) > 1 else None
