def search(titles, term): 
    return [x for x in titles if term.lower() in x.lower()]
