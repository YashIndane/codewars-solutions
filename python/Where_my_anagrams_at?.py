import collections
def anagrams(word, words):
    w = collections.Counter(word)
    return list(filter(lambda x: w == collections.Counter(x), words))
