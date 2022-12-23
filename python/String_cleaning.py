def string_clean(s):
    """
    Function will return the cleaned string
    """
    # Your code here
    q="0123456789"
    w=""
    for x in s:
        if x not in q:
            w+=x
    return w
