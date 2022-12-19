def chain(init_value, functions):
    if functions:
        for x in functions:
            w=x(init_value)
            init_value=w
        return init_value
    else:
        return init_value
