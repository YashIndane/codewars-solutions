def longest(words):
    # Your code here
    return len(max(words, key=lambda z:len(z)))
