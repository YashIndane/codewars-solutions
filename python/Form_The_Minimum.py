def min_value(digits):
    # your code here
    s=sorted(list(set(digits)))
    return int("".join([str(x) for x in s]))
