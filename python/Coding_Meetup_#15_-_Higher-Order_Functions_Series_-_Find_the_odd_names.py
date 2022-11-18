def find_odd_names(lst): 
    # your code here
    def fil(x):
        return sum([ord(v) for v in x['firstName']]) %2 == 1
    return list(filter(fil, lst))
