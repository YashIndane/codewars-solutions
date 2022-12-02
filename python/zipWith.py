def zip_with(fn,a1,a2):
    q = list(zip(a1, a2))
    return [fn(z[0], z[1]) for z in q]
