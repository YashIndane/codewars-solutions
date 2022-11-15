def all_continents(lst): 
    # your code here
    return set([x['continent'] for x in lst]) == set(['Africa', 'Americas', 'Asia', 'Europe', 'Oceania'])
