def count_positives_sum_negatives(arr):
    
    if len(arr) > 0 :
     s = [x for x in arr if x > 0]
     x = [v for v in arr if v < 0]
    
     return [len(s) , sum(x)]
    else : 
        return []
