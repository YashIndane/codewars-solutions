def alphabetic(s):
    for i in range(0, len(s)-1):
        if ord(s[i]) > ord(s[i+1]):
            return False
    return True
