def disemvowel(string_):
    return "".join(filter(lambda x: x not in 'aeiouAEIOU', string_))
