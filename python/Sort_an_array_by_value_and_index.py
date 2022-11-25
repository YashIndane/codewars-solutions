def sort_by_value_and_index(arr):
    d = dict(enumerate(arr))
    return [v[1] for v in sorted(d.items(), key=lambda x: (x[0]+1)*x[1])]
