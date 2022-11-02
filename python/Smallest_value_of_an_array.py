def find_smallest(numbers,to_return):
    # Enter your code here!
    w=min(numbers)
    if to_return=='value': return w
    else: return numbers.index(w)
