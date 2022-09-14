def itemgetter(item):
    return item['name']
    
def get_names(data):
    return list(map(itemgetter, data))
