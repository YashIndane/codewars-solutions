def count_developers(lst):
    # Your code here
    fil = lambda x: x['language'] == 'JavaScript' and x['continent'] == 'Europe'
    return len(list(filter(fil, lst)))
