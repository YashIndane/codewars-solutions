def vowel_change(txt, vow):
    return txt.translate(txt.maketrans('aeiou', vow*5))
