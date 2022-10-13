def find_multiples(integer, limit):
    # Your code here!
    return [x for x in list(range(1, limit+1)) if x%integer==0]
