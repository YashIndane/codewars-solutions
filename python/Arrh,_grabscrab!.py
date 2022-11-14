from collections import Counter
def grabscrab(word, possible_words):
    # your code here
    def fil(x):
        return Counter(word) == Counter(x)
    return list(filter(fil, possible_words))
