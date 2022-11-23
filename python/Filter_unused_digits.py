def unused_digits(*args):
    k="".join(map(str, args))
    return "".join(map(str, sorted(filter(lambda x: str(x) not in k, range(10)))))
