def capital(capitals): 
    # your code here
    w = []
    for d in capitals:

        w.append(f"The capital of {d.get('state') or d.get('country')} is {d['capital']}")
    return w
