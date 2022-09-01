def words_to_sentence(words):
    w = ''
    for k in words : w += k + ' '
    return w[:len(w) - 1]
