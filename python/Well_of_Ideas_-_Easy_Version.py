def well(x):
    #your code here
    return 'Publish!' if 3 > x.count('good') >= 1 else 'I smell a series!' if x.count('good') > 2 else 'Fail!'
