from collections import Counter
def order_food(lst): 
    # your code here
    return dict(Counter([x['meal'] for x in lst]))
