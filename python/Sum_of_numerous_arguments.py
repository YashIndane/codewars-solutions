def find_sum(*args):
    #your code here
    if args:
        if all([x>=0 for x in args]):
            return sum(args)
        else:
            return -1
    return 0
