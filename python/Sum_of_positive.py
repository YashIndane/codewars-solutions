def positive_sum(arr):
    try : 
        return sum([x for x in arr if x > 0])
    except :
        return 0
