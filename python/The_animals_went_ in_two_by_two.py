def two_by_two(animals):
    #your code goes here
    if animals:
        q=dict(__import__("collections").Counter(animals))
        q=dict(filter(lambda x: x[1]>1, q.items()))
        q={x:2 for x,y in q.items()}
        return q
        
    else:
        return False
