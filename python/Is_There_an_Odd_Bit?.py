def any_odd(x):
    # Write code here...
    w = bin(x).replace("0b", "")[::-1]
    for i ,k in enumerate(w):
        if i == 0:
            pass
        else:
            if i%2 == 1 and k == "1":
                return True
    return False
