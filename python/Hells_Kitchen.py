def gordon(a):
    # your code here
    w='!!!! '.join([s for s in a.upper().split()]) + '!!!!'
    return w.translate(w.maketrans('AEIUO', '@****'))
