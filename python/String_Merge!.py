def string_merge(string1, string2, letter):
    return string1[:string1.index(letter)] + letter + string2[string2.index(letter)+1:]
