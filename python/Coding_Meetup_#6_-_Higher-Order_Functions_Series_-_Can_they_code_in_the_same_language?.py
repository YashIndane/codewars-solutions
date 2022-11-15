def is_same_language(lst): 
    # your code here
    return len(set([x['language'] for x in lst])) == 1
