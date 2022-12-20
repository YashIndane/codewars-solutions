def sum_array(arr):
    #your code here
    return sum(arr)-sum([min(arr),max(arr)]) if arr and len(arr)>1 else 0
