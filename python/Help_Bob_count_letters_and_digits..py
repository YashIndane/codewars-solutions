def count_letters_and_digits(s):
    q="0123456789abcdefghijklmnopqrstuvwxyz"
    q=q+q.upper()
    w=0
    for x in s:
        if x in q:
            w+=1
    return w
