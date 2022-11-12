def capitals(word):
    #your code here
    return [i for i, x in enumerate(word) if x.isupper()]
