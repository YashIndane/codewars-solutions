def sort_my_string(s):
    # Your code here =)
    e=""
    o=""
    for i, x in enumerate(s):
        if i%2==0:
            e+=x
        else:
            o+=x
    return e+" "+o
