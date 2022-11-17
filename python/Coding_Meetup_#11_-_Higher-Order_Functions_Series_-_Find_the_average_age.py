def get_average(lst): 
    # your code here
    return round(sum(x['age'] for x in lst)/len(lst))
