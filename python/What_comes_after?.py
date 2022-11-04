def comes_after(st, l): 
    # your code here
    e=''
    for j in range(len(st)-1):
        if st[j].lower()==l.lower():
            e+=st[j+1] if st[j+1].isalpha() else ''
    return e
