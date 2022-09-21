def find_longest(string):
    return len(sorted(string.split(" "), key=lambda x: len(x))[-1])
