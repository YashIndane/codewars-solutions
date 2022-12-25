def create_array_of_tiers(n):
    # your awesome code here
    n=str(n)
    a=[]
    for x in range(1, len(n)+1):
        a.append(n[:x])
    return a 
