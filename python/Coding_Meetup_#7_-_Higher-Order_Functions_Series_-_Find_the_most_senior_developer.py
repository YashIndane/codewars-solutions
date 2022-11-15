def find_senior(lst): 
    # your code here
    age = max([x['age'] for x in lst])
    return [x for x in lst if x['age'] == age]
