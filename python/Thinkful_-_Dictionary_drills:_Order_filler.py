def fillable(stock, merch, n):
    # Your code goes here.
    try:
        if stock[merch] >= n:
            return True
        else:
            return False
    except: return False
