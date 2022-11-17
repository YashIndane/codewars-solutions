def is_ruby_coming(lst): 
    # your code here
    for x in lst:
        if x['language'] == 'Ruby': return True
    return False
