def enough(cap, on, wait):
    # Your code here
    q = wait-(cap - on)
    if q >= 0:
        return q
    else:
        return 0
