def big(x):
    q="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum([q.index(c)+1 for c in x])
def battle(x, y):
    #Let the battle begin!
    xs=big(x)
    ys=big(y)
    if xs==ys:
        return "Tie!"
    else:
        return x if xs>ys else y
