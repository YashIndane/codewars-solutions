def greet_developers(lst): 
    # your code here
    for x in lst:
        x['greeting'] = f"Hi {x['firstName']}, what do you like the most about {x['language']}?"
    return lst
