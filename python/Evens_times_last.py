def even_last(numbers): 
    # your code here
    if len(numbers) != 0:
        d = 0
        for i, x in enumerate(numbers):
            if i%2==0:
                d+=x 
        return d*numbers[-1]
    else:
        return 0
