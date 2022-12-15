def is_divisible(*args):
    #your code here
    q=args[0]
    return all([q%z==0 for z in args[1:]])
