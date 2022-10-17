def vowel_indices(word):
    return [i+1 for i, x in enumerate(word) if x in 'AEIOUaeiuoYy']
