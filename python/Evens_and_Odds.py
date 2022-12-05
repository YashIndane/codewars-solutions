def evens_and_odds(n):
    #your code here
    if n%2 == 1:
        h=hex(n)
        h.lower()
        return h[2:]
    else:
        return bin(n)[2:]
