def most_frequent_item_count(collection):
    # Do your magic. :)
    if collection:
        return max([collection.count(x) for x in collection])
    else:
        return 0
