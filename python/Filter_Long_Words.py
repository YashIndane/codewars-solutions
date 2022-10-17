def filter_long_words(sentence, n):
      return [x for x in sentence.split() if len(x)>n]
