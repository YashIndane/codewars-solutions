def dont_give_me_five(start,end):
    # your code here
    return len(list(filter(lambda x: "5" not in str(x), range(start, end+1))))
